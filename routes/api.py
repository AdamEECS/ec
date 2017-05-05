from models.user import User
from models.product import Product
from models.order import Order
from routes import *
from flask import current_app as app
from decimal import Decimal

main = Blueprint('api', __name__)


@main.route('/cart_add', methods=['POST'])
@login_required
def cart_add():
    u = current_user()
    product_id = request.json.get('product_id', None)
    response = dict(
        status='error',
    )
    if product_id:
        product_id = str(product_id)
        count = u.cart.get(product_id, 0)
        count += 1
        u.cart[product_id] = count
        u.save()
        response['status'] = 'OK'
    return json.dumps(response)


@main.route('/cart_sub', methods=['POST'])
@login_required
def cart_sub():
    u = current_user()
    product_id = request.json.get('product_id', None)
    response = dict(
        status='error',
    )
    if product_id:
        product_id = str(product_id)
        count = u.cart.get(product_id, 0)
        count -= 1
        u.cart[product_id] = count
        if count <= 0:
            u.cart.pop(product_id)
        u.save()
        response['status'] = 'OK'
    return json.dumps(response)


@main.route('/callback', methods=['POST'])
@login_required
def callback():
    # u = current_user()
    form = request.form
    with open('log.txt', 'ab+') as f:
        f.write(form)
