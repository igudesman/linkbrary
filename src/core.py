from telebot import logger, TeleBot

import logging
import configs
import abc


class ABC(TeleBot):
    def __init__(self):
        super().__init__(configs.TELEGRAM_TOKEN)

    @staticmethod
    def enable_logging():
        _ = logger
        logger.setLevel(logging.DEBUG)


class Interface(metaclass=abc.ABCMeta):
    def hello(self):
        raise NotImplementedError()


