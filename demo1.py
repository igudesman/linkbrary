from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
import logging
import config
import random
from typing import Dict

def main():

    updater = Updater(token=config.telegram_api_key)

    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # user id to list of links
    users_storage = {}


    def start(update, context):
        print(context)
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def get_all_links(update, context):
        users_links = str(context.user_data['links'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=users_links)

    def get_random_link(update, context):
        users_links = context.user_data['links']
        link_name = users_links[random.randrange(0, len(users_links))]
        context.bot.send_message(chat_id=update.effective_chat.id, text=link_name)

    def save_link(update, context):
        if 'links' not in context.user_data.keys():
            context.user_data['links'] = []
        # user_id = update.message.from_user['id']
        context.user_data['links'].append(update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Your link saved!")

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    getlinks_handler = CommandHandler('get', get_all_links)
    dispatcher.add_handler(getlinks_handler)

    getrand_handler = CommandHandler('getrand', get_random_link)
    dispatcher.add_handler(getrand_handler)

    savelink_handler = MessageHandler(Filters.text & (~Filters.command), save_link)
    dispatcher.add_handler(savelink_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()