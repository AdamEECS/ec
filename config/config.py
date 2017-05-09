from pymongo import *

config_dict = dict(
    USER_AVATAR_DIR='static/user_avatar/',
    PRODUCT_PIC_DIR='static/product_pic/',
    PRODUCT_PIC_EXT='png',
    CDN_URL='http://opguqe876.bkt.clouddn.com/',
    CDN_USER_AVATAR_DIR='/user_avatar/',
    CDN_PRODUCT_PIC_DIR='/product_pic/',
    CDN_BUCKET='buy-suzumiya',
    QINIU_CALLBACK_URL='https://buy.suzumiya.cc/callback/all',
    PIC_UPLOAD_URL='https://up-z1.qbox.me/',
    SEND_EMAIL_URL='https://api.mailgun.net/v3/mg.suzumiya.cc/messages',
    SEND_EMAIL_FROM='Suzumiya <no-replay@mg.suzumiya.cc>',
)

# mongodb config
db_name = 'mongo_ec'
client = MongoClient("mongodb://localhost:27017")
db = client[db_name]
