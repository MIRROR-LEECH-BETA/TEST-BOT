from pymongo import MongoClient

client = MongoClient("mongodb+srv://JP:JP@cluster0.auy64.mongodb.net/?retryWrites=true&w=majority")

users = client['main']['bots']


def already_db(user_id):
        user = users.find_one({"bot_token" : str(user_id)})
        if not user:
            return False
        return True

def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"bot_token": str(user_id)}) 

def remove_user(user_id):
    in_db = already_db(user_id)
    if not in_db:
        return 
    return users.delete_one({"bot_token": str(user_id)})

def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs
