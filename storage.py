import os
import pymongo
import configs
import copy

CLIENT = pymongo.MongoClient(
    f"mongodb+srv://"
    f"{configs.MONGO_USERNAME}"
    f":{configs.MONGO_PASSWORD}"
    f"@{configs.MONGO_HOST}"
)


def get_user(chat_id):
    db = CLIENT['users']
    collection_name = db['user_info']
    if collection_name.count_documents({'chat_id': chat_id}) == 0:
        return {}
    else:
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
    if result.upserted_id is None:
        return False
    else:
        return True


def get_conversation(chat_id):
    db = CLIENT['users']
    collection_name = db['conversation_status']
    status = collection_name.find({'chat_id': chat_id}).next()['status']
    return status


def add_link(link_params):
    print("CONNECTING TO DB")
    # save link into the database
    db = CLIENT['users']
    collection = db['links']
    collection.insert_one(link_params)
    return True


def get_random_link(chat_id):
    # retrieve random link from a database
    pass
