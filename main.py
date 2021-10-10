from core import ABC, Interface
import configs
from analyzers import LinkAnalyzer
import errors
import storage


def authorized(func):
    def wrapper(*args, **kwargs):
        chat_id = args[0].chat.id
        if storage.get_user(chat_id):
            func(*args, **kwargs)
        else:
            BotInterface.bot.send_message(chat_id, 'You have to be authorized! Please, use _/auth_ to continue.')
    return wrapper


class BotInterface(Interface):
    bot = ABC()
    bot.enable_logging()
    monkey_link_analyzer = LinkAnalyzer()

    @staticmethod
    def listen_mode():
        BotInterface.bot.polling(none_stop=True, interval=0)

    @staticmethod
    @bot.message_handler(commands=['help'])
    def help(message):
        BotInterface.bot.send_message(message.chat.id, configs.HELP_MESSAGE, parse_mode='Markdown')

    @staticmethod
    @bot.message_handler(commands=['auth'])
    def help(message):
        BotInterface.bot.send_message(message.chat.id, configs.HELP_MESSAGE, parse_mode='Markdown')

    @staticmethod
    @bot.message_handler(commands=['start'])
    @authorized
    def start(message):
        BotInterface.bot.send_message(message.chat.id, 'Привет, чем я могу тебе помочь?')

    @staticmethod
    @bot.message_handler(content_types=['text'])
    def add_link(message):
        try:
            parsed_text = BotInterface.monkey_link_analyzer.get_link_text(message.text)
            estimated_time = BotInterface.monkey_link_analyzer.time_estimator(parsed_text)
            topic = BotInterface.monkey_link_analyzer.get_topic(parsed_text)
            response = topic.body[0]['classifications'][0]['tag_name']
            response = f'The classified topic: _{response}_\nEstimated time: {estimated_time}min.'
        except errors.InvalidUrl:
            response = 'Invalid URL!'
        except KeyError:
            response = 'Oops! Something went wrong. Try to provide topic explicitly.'

        BotInterface.bot.send_message(message.chat.id, response, parse_mode='Markdown')


if __name__ == '__main__':
    BotInterface.listen_mode()
