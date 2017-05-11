from routes import *
from models.product import Product
from models.order import Order
from models.user import User
from flask import current_app as app

import qiniu
from config import key

q = qiniu.Auth(key.qiniu_access_key, key.qiniu_secret_key)

main = Blueprint('admin', __name__)


# ------------------------- 产品管理 --------------------------
@main.route('/product_new')
@admin_required
def product_new_page():
    u = current_user()
    return render_template('admin/product_new.html', u=u)


@main.route('/product_new', methods=['POST'])
@admin_required
def product_new():
    u = current_user()
    form = request.form
    status, msgs = Product.valid(form)
    if status is True:
        p = Product.new(form)
        return redirect(url_for('admin.product', uuid=p.uuid))
    else:
        return render_template('admin/product_new.html', msgs=msgs, u=u)


@main.route('/products')
@admin_required
def products():
    u = current_user()
    ms = Product.all()
    ms.reverse()
    return render_template('admin/products.html', ms=ms, u=u)


@main.route('/products', methods=['POST'])
@admin_required
def products_search():
    u = current_user()
    form = request.form
    ms = Product.search_or(form)
    ms.reverse()
    return render_template('admin/products.html', u=u, ms=ms)


@main.route('/product/<uuid>')
@admin_required
def product(uuid):
    u = current_user()
    p = Product.find_one(uuid=uuid)
    policy = {
        'callbackUrl': app.config['QINIU_CALLBACK_URL'],
        'callbackBody': 'filename=$(fname)&filesize=$(fsize)&route=$(x:route)&',
        'mimeLimit': 'image/*',
    }
    t = timestamp()
    qiniu_key = '{}{}_{}.{}'.format(app.config['CDN_PRODUCT_PIC_DIR'], uuid, t, app.config['PRODUCT_PIC_EXT'])
    u.token = q.upload_token(app.config['CDN_BUCKET'], key=qiniu_key, policy=policy)
    u.upload_url = app.config['PIC_UPLOAD_URL']
    u.key = qiniu_key
    u.url = url_for('admin.ajax_pic', uuid=uuid)
    return render_template('admin/product.html', p=p, u=u)


@main.route('/product/<uuid>', methods=['POST'])
@admin_required
def product_update(uuid):
    p = Product.find_one(uuid=uuid)
    form = request.form
    p.update(form)
    return redirect(url_for('admin.product', uuid=p.uuid))


@main.route('/set_product_pic_url/<uuid>', methods=['POST'])
@admin_required
def set_product_pic_url(uuid):
    p = Product.find_one(uuid=uuid)
    url = request.form.get('file_url')
    p.set_pic_url(url)
    return redirect(url_for('admin.product', uuid=p.uuid))


@main.route('/ajax_pic/<uuid>', methods=['POST'])
@admin_required
def ajax_pic(uuid):
    p = Product.find_one(uuid=uuid)
    qiniu_key = request.form.get('key')
    p.qiniu_pic(qiniu_key)
    return redirect(url_for('admin.product', uuid=p.uuid))


@main.route('/delete/<int:id>')
@admin_required
def product_delete(id):
    # p = Model.get(id)
    # p.delete()
    # TODO 先不让删
    return redirect(url_for('admin.products'))


# ------------------------- 用户管理 --------------------------
@main.route('/users')
@admin_required
def users():
    u = current_user()
    ms = User.all()
    return render_template('admin/users.html', ms=ms, u=u)


@main.route('/users', methods=['POST'])
@admin_required
def users_search():
    u = current_user()
    form = request.form
    ms = User.search_or(form)
    return render_template('admin/users.html', u=u, ms=ms)


@main.route('/user/<int:id>')
@admin_required
def user(id):
    u = current_user()
    m = User.get(id)
    ps = m.get_cart_detail()
    return render_template('admin/user.html', m=m, ps=ps, u=u)


@main.route('/user/delete/<int:id>')
@admin_required
def user_delete(id):
    # m = User.get(id)
    # m.delete()
    # TODO 先不让删
    return redirect(url_for('admin.users'))


@main.route('/user/update/<int:id>', methods=['POST'])
@admin_required
def user_update(id):
    m = User.get(id)
    form = request.form
    m.update_user(form)
    return redirect(url_for('admin.user', id=m.id))


# ------------------------- 订单管理 --------------------------
@main.route('/orders')
@admin_required
def orders():
    u = current_user()
    ms = Order.all()
    ms.reverse()
    return render_template('admin/orders.html', ms=ms, u=u)


@main.route('/orders', methods=['POST'])
@admin_required
def orders_search():
    u = current_user()
    form = request.form
    ms = Order.search_or(form)
    ms.reverse()
    return render_template('admin/orders.html', u=u, ms=ms)


@main.route('/order/<orderNo>')
@admin_required
def order(orderNo):
    u = current_user()
    o = Order.find_one(orderNo=orderNo)
    o.user = User.get(o.user_id)
    return render_template('admin/order.html', o=o, u=u)


@main.route('/order_delivery/<orderNo>')
@admin_required
def order_delivery(orderNo):
    o = Order.find_one(orderNo=orderNo)
    o.delivery()
    return redirect(url_for('admin.orders'))

# @main.route('/root')
# @login_required
# def root_set():
#     root = User.find_one(username='root')
#     root.role = 'admin'
#     root.save()
#     return redirect(url_for('admin.products'))
#
#
# @main.route('/uuid_reset_all')
# @admin_required
# def order_no_reset():
#     os = Order.all()
#     us = User.all()
#     ps = Product.all()
#     for o in os:
#         o.set_uuid('orderNo')
#         o.set_uuid()
#     for u in us:
#         u.set_uuid()
#     for p in ps:
#         p.set_uuid()
#     return redirect(url_for('admin.products'))
#
#
# @main.route('/clear_order_items')
# @admin_required
# def clear_order_items():
#     os = Order.all()
#     for o in os:
#         o.items = []
#         o.save()
#     return redirect(url_for('admin.products'))


@main.route('/clear_orders')
@admin_required
def clear_orders():
    os = Order.all()
    for o in os:
        o.delete()
    return redirect(url_for('admin.products'))


@main.route('/clear_carts')
@admin_required
def clear_carts():
    us = User.all()
    for u in us:
        u.cart_clear()
    return redirect(url_for('admin.products'))