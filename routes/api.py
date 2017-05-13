from routes import *

main = Blueprint('api', __name__)


@main.route('/cart/add', methods=['POST'])
@login_required
def cart_add():
    u = current_user()
    product_uuid = request.json.get('product_uuid', None)
    response = dict(
        status='error',
    )
    u.cart_add(product_uuid)
    response['status'] = 'OK'
    return json.dumps(response)


@main.route('/cart/sub', methods=['POST'])
@login_required
def cart_sub():
    u = current_user()
    product_uuid = request.json.get('product_uuid', None)
    response = dict(
        status='error',
    )
    u.cart_sub(product_uuid)
    response['status'] = 'OK'
    return json.dumps(response)
