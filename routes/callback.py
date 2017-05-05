from models.user import User
from models.product import Product
from models.order import Order
from routes import *
from flask import current_app as app
from decimal import Decimal
import qiniu

main = Blueprint('callback', __name__)
access_key = '4inGYVb4FYcXg5V9suieWkx80yKefQphTpJ4rELS'
secret_key = 'LqW9ei2fXQDHR9UQEg_Ay-6qff00dwTmNu9tDpLz'
q = qiniu.Auth(access_key, secret_key)
bucket_name = 'buy-suzumiya'


@main.route('/callback', methods=['POST'])
def callback():
    form = request.form


@main.route('/product_add', methods=['POST'])
def product_add():
    form = request.form
    header = request.headers
    print(header)
    print(form)
    r = {"success": True}
    return json.dumps(r)

