from telebot import logger, TeleBot
from monkeylearn import MonkeyLearn
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


class Analyzer:
    def __init__(self):
        self.monkey = MonkeyLearn(configs.MONKEY_TOKEN)

    def get_topic(self, text):
        raise NotImplementedError()

    def time_estimator(self, text):
        raise NotImplementedError()
