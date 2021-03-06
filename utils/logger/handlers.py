import logging.handlers
import time
from queue import Queue

import requests

from memflask.logger.formatter import HTMLFormatter, MarkdownFormatter

__all__ = ("TelegramHandler",)

HTML = "html"
MARKDOWN = "markdownv2"

FORMATTERS = {
    HTML: HTMLFormatter,
    MARKDOWN: MarkdownFormatter
}

logger = logging.getLogger()


class TelegramHandler(logging.handlers.QueueHandler):
    """
    Base handler which instantiate and start queue listener and message dispatcher
    """

    def __init__(self, token: str, chat_ids: list, webhook_url=None, cert=None, key=None, format: str = MARKDOWN,
                 disable_notifications: bool = False, disable_preview: bool = False):
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


class LogMessageDispatcher(logging.Handler):
    """
    Separate thread for a message dispatching
    """
    TIMEOUT = 13  # seconds
    MAX_MSG_LEN = 3000
    API_CALL_INTERVAL = 1 / 30  # 30 calls per second

    def __init__(self, token: str, chat_ids: list, url=None, cert=None, key=None, disable_notifications: bool = False,
                 disable_preview: bool = False):
        """
        See Handler args
        """
        self.token = token
        self.chat_ids = chat_ids
        self.disable_notifications = disable_notifications
        self.disable_preview = disable_preview
        self.session = requests.Session()
        self.url_custom = url
        self.cert = cert
        self.key = key
        super().__init__()

    @property
    def url(self):
        if self.url_custom:
            return f"{self.url_custom}" + "/bot{token}/sendMessage?chat_id={chat_id}&text={text}&parse_mode={mode}&" \
                                          "disable_web_page_preview={disable_web_page_preview}&disable_notifications={disable_notifications}"
        return "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&parse_mode={mode}&" \
               "disable_web_page_preview={disable_web_page_preview}&disable_notifications={disable_notifications}"

    def handle(self, record):
        """
        Perform message splitting in case if it is big
        """
        record = self.format(record)

        if len(record) > self.MAX_MSG_LEN:

            # telegram max length of text is 4096 chars, we need to split our text into chunks

            start_chars, end_chars = "", self.formatter.BLOCK_OPEN
            start_idx, end_idx = 0, self.MAX_MSG_LEN - len(end_chars)
            # don't forget about markdown symbols (```)
            new_record = record[start_idx:end_idx]

            while new_record:
                # remove whitespaces, markdown fmt symbols and a carriage return
                new_record = start_chars + new_record.rstrip("` \n") + end_chars
                self.emit(new_record.replace("#", "%23"))

                start_chars, end_chars = self.formatter.BLOCK_OPEN, self.formatter.BLOCK_CLOSE
                start_idx, end_idx = end_idx, end_idx + self.MAX_MSG_LEN - (len(start_chars) + len(end_chars))
                new_record = record[start_idx:end_idx]
        else:
            self.emit(record)

    def emit(self, record):
        for chat_id in self.chat_ids:
            url = self.url.format(
                token=self.token,
                chat_id=chat_id,
                mode=self.formatter.MODE,
                text=record,
                disable_web_page_preview=self.disable_preview,
                disable_notifications=self.disable_notifications
            )
            if self.cert and self.key:
                cert = (self.cert, self.key)
                response = self.session.get(url, timeout=self.TIMEOUT, cert=cert)
            else:
                response = self.session.get(url, timeout=self.TIMEOUT)
            if not response.ok:
                logger.warning("Telegram log dispatching failed with status code '%s'" % response.status_code)
                logger.warning("Response is: %s" % response.text)

            # telegram API restrict more than 30 calls per second, this is a very pessimistic sleep,
            # but should work as a temporary workaround
            time.sleep(self.API_CALL_INTERVAL)

    def __del__(self):
        self.session.close()
