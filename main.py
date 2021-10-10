from core import ABC, Interface
import configs
from analyzers import LinkAnalyzer
import errors
import copy
import storage
import urllib.parse


def authorized(func):
    def wrapper(*args, **kwargs):
        chat_id = args[0].chat.id
        if storage.get_user(chat_id):
            func(*args, **kwargs)
        else:
            BotInterface.bot.send_message(chat_id, 'You have to be authorized! Please, use _/auth_ to continue.', parse_mode='Markdown')
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
    def auth(message):
        BotInterface.bot.send_message(message.chat.id, configs.AUTH, parse_mode='Markdown')
        storage.add_conversation(message.chat.id, 'AUTH')
    
    @staticmethod
    @bot.message_handler(commands=['stop'])
    def stop(message):
        storage.add_conversation(message.chat.id, 'USE')

    @staticmethod
    @bot.message_handler(commands=['start'])
    @authorized
    def start(message):
        BotInterface.bot.send_message(message.chat.id, 'Use _/help_ to know more about Linkbrary', parse_mode='Markdown')

    @staticmethod
    @bot.message_handler(content_types=['text'])
    def add_link(message):
        if storage.get_conversation(message.chat.id) == 'AUTH':
            storage.add_user(message.chat.id, message.text, '')
            storage.add_conversation(message.chat.id, 'USE')
            BotInterface.bot.send_message(message.chat.id, 'The agreement has been sent!')
        else:
            try:
                parsed_text = BotInterface.monkey_link_analyzer.get_link_text(message.text)
                # extract link features
                url_title = urllib.parse.urlparse(message.text).netloc
                estimated_time = BotInterface.monkey_link_analyzer.time_estimator(parsed_text)
                topic = BotInterface.monkey_link_analyzer.get_topic(parsed_text)
                link_topic = topic.body[0]['classifications'][0]['tag_name']
                response = f'Your link saved: {url_title}\n' \
                           f'The classified topic: _{link_topic}_\n' \
                           f'Estimated time: {estimated_time}min.'

                # save link to the database
                link_params = copy.copy(configs.LINK_TEMPLATE)
                link_params['title'] = url_title
                link_params['url'] = message.text
                link_params['chat_id'] = message.chat.id
                link_params['topics'] = link_topic
                link_params['ETR'] = estimated_time

                storage.add_link(link_params)
            except errors.InvalidUrl:
                response = 'Invalid URL!'
            except KeyError:
                response = 'Oops! Something went wrong. Try to provide topic explicitly.'

            BotInterface.bot.send_message(message.chat.id, response, parse_mode='Markdown')


if __name__ == '__main__':
    BotInterface.listen_mode()
