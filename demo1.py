from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
import logging
import config

updater = Updater(token=config.telegram_api_key)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
