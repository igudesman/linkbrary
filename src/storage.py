"""
Module for connection with database strorage - CRUD operations.
"""
import ssl
import copy
import pymongo
import configs
from link import Link

CLIENT = pymongo.MongoClient(
    f"mongodb+srv://"
    f"{configs.MONGO_USERNAME}"
    f":{configs.MONGO_PASSWORD}"
    f"@{configs.MONGO_HOST}",
    ssl_cert_reqs=ssl.CERT_NONE
)


def get_user(chat_id):
    db = CLIENT['users']
    collection_name = db['user_info']
    if collection_name.count_documents({'chat_id': chat_id}) == 0:
        return {}
    return collection_name.find({'chat_id': chat_id}).next()


def add_user(chat_id, email, passphrase):
    try:
        new_user = copy.copy(configs.USER_FORM)
        new_user['chat_id'] = chat_id
        new_user['email'] = email
        new_user['passphrase'] = passphrase
        db = CLIENT['users']
        collection_name = db['user_info']
        collection_name.insert_one(new_user)
        return True
    except:
        return False


def add_conversation(chat_id, status):
    db = CLIENT['users']
    collection_name = db['conversation_status']
    result = collection_name.update_one(
        {'chat_id': chat_id},
        {"$set": {'status': status}},
        upsert=True
    )
    return result.upserted_id is not None


def get_conversation(chat_id):
    db = CLIENT['users']
    collection_name = db['conversation_status']
    status = collection_name.find({'chat_id': chat_id}).next()['status']
    return status


def add_link(link):
    # save link into the database
    db = CLIENT['users']
    collection = db['links']
    collection.insert_one(link)
    return True


def get_random_link(chat_id):
    # retrieve random link from a database
    db = CLIENT['users']
    collection = db['links']
    random_link = list(collection.aggregate([
        {'$match': {'chat_id': chat_id, 'viewed': False}},
        {'$sample': {'size': 1}}
    ]))
    if len(random_link) == 0:
        return Link()
    random_link = random_link[0]
    link_id = random_link['_id']
    collection.update_one(
        {'_id': link_id},
        {"$set": {'viewed': True}},
        upsert=True
    )
    return Link(dict_params=random_link)
