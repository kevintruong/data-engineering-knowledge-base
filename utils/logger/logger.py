# Copyright (c) 2020 Vu Truong - kevin.truong.ds@gmail.com all rights reserved
#
import logging
import os
import sys
from datetime import datetime
from logging.config import dictConfig

import stackprinter

from memflask.logger.handlers import TelegramHandler


class VerboseExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        msg = stackprinter.format(exc_info)
        msg_indented = '    ' + '\n    '.join(msg.split('\n')).strip()
        return msg_indented


def configure_exception_logger(filename,
                               tg_token,
                               report_ids: [],
                               webhook_url=None,
                               cert=None,
                               key=None,
                               logger_name=None):
    fmt = '%(asctime)s %(levelname)s: %(message)s'
    formatter = VerboseExceptionFormatter(fmt)

    handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)

    telegram_log_handler = TelegramHandler(tg_token, report_ids, webhook_url, cert, key,
                                           disable_notifications=True)

    logger = logging.getLogger(logger_name)
    logger.addHandler(handler)
    logger.addHandler(telegram_log_handler)
    # add telegram exception handle

    return logger


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - [%(filename)s:%(lineno)d:%(levelname)s] - %(message)s"
        },
        "root": {
            "format": "ROOT - %(asctime)s - [%(filename)s:%(lineno)d:%(levelname)s] - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default"
        },
        "root_console": {
            "class": "logging.StreamHandler",
            "formatter": "root"
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': '/tmp/debug_tool.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },

    },
    "loggers": {
        "app": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": False
        }
    },
    "root": {
        "handlers": ["file"],
        "level": "INFO"
    }
}

config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "memflask.logger.formatters.MarkdownFormatter",
            "fmt": " *%(levelname)s* _%(name)s : %(funcName)s_"
        }
    },
    "handlers": {
        "telegram": {
            "class": "memflask.logger.handlers.Handler",
            # "token": "bot_token",
            # "chat_ids": [123456789, -1234567891011],
            "formatter": "default"
        }
    },
    "loggers": {
        "tg": {
            "level": "INFO",
            "handlers": ["telegram", ]
        }
    }
}

process_name = os.path.basename(sys.argv[0]).split(".")[0]
app_debug_log_file = '/tmp/debug_info_{}_{:%Y-%m-%d}.log'.format(process_name, datetime.now())
app_exp_log_file = '/tmp/exp_info_{}_{:%Y-%m-%d}.log'.format(process_name, datetime.now())
LOGGING_CONFIG['handlers']['file']['filename'] = app_debug_log_file
dictConfig(LOGGING_CONFIG)

app_logger = logging.getLogger("app")
