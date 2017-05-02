from pymongo import *

user_avatar_dir = 'static/user_avatar/'
product_pic_dir = 'static/product_pic/'
config_dict = dict(
    USER_AVATAR_DIR='static/user_avatar/',
    PRODUCT_PIC_DIR='static/product_pic/',
    PRODUCT_PIC_EXT='png',
)

# mongodb config
db_name = 'mongo_ec'
client = MongoClient("mongodb://localhost:27017")
db = client[db_name]
