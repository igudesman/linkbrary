import os

HELP_MESSAGE = '''
*Linkbrary!*
Send me (or forward from other chats or channels) any messages that contain links. I will save and aggregate all the links.
You can also add tags, for example like this:  https://google.com #longread #ai

_Some useful commands:
/help — Help
/settings — Bot Settings
_
'''
TELEGRAM_TOKEN = os.environ['TOKEN']
MONKEY_TOKEN = os.environ['MONKEY']
TOPIC_CLASSIFIER = os.environ['TOPIC_CLASSIFIER']
MONGO_HOST = os.environ['MONGO_HOST']
MONGO_USERNAME = os.environ['MONGO_USERNAME']
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']

USER_FORM = {
    'chat_id': '',
    'passphrase': '',
    'email': '',
}

AUTH = '''
*Data Processing Agreement*
Provide your _email_ address that will be used for this account. We will send you the agreement for review. Follow the instructions in the email.
'''
