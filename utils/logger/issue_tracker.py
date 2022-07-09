import json
import logging.handlers

import psycopg2
import stackprinter

from memflask.config import config

"""
create view error_report as 
select 
  error_id, 
  max(
    concat(
      coalesce( ( (body ->> 'trace'):: jsonb ->> 'exception' ):: jsonb ->> 'class', 'Error' ), 
      ': ', 
      ( (body ->> 'trace'):: jsonb ->> 'exception' ):: jsonb ->> 'message', 
      (body ->> 'message'):: jsonb ->> 'body' ) 
      ) as error, 
  count(*) as occurences, 
  max(timestamp) as last_seen, 
  max( array_to_string( 
            array( select concat( el ->> 'filename', ':', el ->> 'lineno' ) 
            from jsonb_array_elements( ( (body ->> 'trace'):: jsonb ->> 'frames' ):: jsonb ) as el limit 4
          ), ', ' ) ) 
      as trace, 
  max(environment) as environment, 
  max(custom ->> 'revision') as revision 
from 
  errors 
group by 
  error_id 
order by 
  last_seen desc;
"""


def connect_db():
    return psycopg2.connect(config['database']['sql_uri'])


def create_table():
    conn = connect_db()
    sql = """
      CREATE TABLE if not exists errors (
        id BIGSERIAL PRIMARY KEY,
        body JSONB NOT NULL,
        error_id VARCHAR GENERATED ALWAYS AS (md5(body::TEXT)) STORED NOT NULL,
        timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT(NOW() AT TIME ZONE 'utc') NOT NULL,
        level VARCHAR
      );
      CREATE INDEX idx_errors_timestamp ON errors(timestamp);
      CREATE INDEX idx_errors_error_id ON errors(error_id);
    """
    with conn.cursor() as curs:
        curs.execute(sql)
    conn.commit()
    conn.close()


try:
    create_table()
except Exception as e:
    print(e)


def write_to_db(data):
    conn = connect_db()
    with conn.cursor() as curs:
        res = curs.execute("""
        INSERT INTO errors 
        ( body,
        level) 
        VALUES (%s,%s)
        """, (json.dumps(data.get("body")),
              data.get("level"),
              ), )
        conn.commit()
        conn.close()


class IssueTrackerFormatter(logging.Formatter):
    FMT = BLOCK_OPEN = BLOCK_CLOSE = None

    def __init__(self, fmt: str = None, *args, **kwargs):
        super().__init__(fmt or self.FMT, *args, **kwargs)

    def format(self, record):
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        record = self.enrich_exception(record)
        return record

    def formatException(self, exc_info):
        msg = stackprinter.format(exc_info)
        msg_indented = '    ' + '\n    '.join(msg.split('\n')).strip()
        return msg_indented

    def enrich_exception(self, record):
        """
        Enrich and do some formatting
        """
        if record.exc_info:
            record.exc_text = self.formatException(record.exc_info)

        if record.stack_info:
            record.exc = self.formatStack(record.stack_info)

        return record


class IssueTrackerHandler(logging.handlers.QueueHandler):
    """
    Base handler which instantiate and start queue listener and message dispatcher
    """

    def __init__(self):
        """
        :param token: telegram bot API token
        :param chat_ids: list of intergers with chat ids
        :param format: message format. Either 'html' or 'markdown'
        :param disable_notifications: enable/disable bot notifications
        :param disable_preview: enable/disable web-pages preview
        """
        queue = Queue()
        super().__init__(queue)

        try:
            formatter = FORMATTERS[format.lower()]
        except Exception:
            raise Exception("TelegramLogging. Unknown format '%s'" % format)

        self.handler = LogMessageDispatcher(token, chat_ids, webhook_url, disable_notifications, disable_preview)
        self.handler.setFormatter(formatter())
        listener = logging.handlers.QueueListener(queue, self.handler)
        listener.start()

    def prepare(self, record):
        return record

    def setFormatter(self, fmt):
        """
        Since we use underlying thread-based handler - we need to set a formatter to it
        """
        self.handler.formatter = fmt
