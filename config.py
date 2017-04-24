from pymongo import *


# key
secret_key = 'ec key i32b*@M>2?s'

user_avatar_dir = 'static/user_avatar/'

# mongodb config
db_name = 'mongo_ec'
client = MongoClient("mongodb://localhost:27017")
db = client[db_name]
