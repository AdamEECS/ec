from models.user import User
from models.product import Product
from models.order import Order
from routes import *
from flask import current_app as app
from decimal import Decimal
import qiniu

main = Blueprint('callback', __name__)

from config import key

q = qiniu.Auth(key.qiniu_access_key, key.qiniu_secret_key)


@main.route('/callback', methods=['POST'])
def callback():
    form = request.form


@main.route('/all', methods=['POST'])
def product_add():
    body = request.get_data()
    body = body.decode('utf-8')
    form = request.form
    auth = request.headers.get('Authorization')
    url = app.config['QINIU_CALLBACK_URL']
    print(form)
    verify = q.verify_callback(auth, url, body)
    if verify:
        print('verify :', verify)
    r = {"success": True}
    return json.dumps(r)
