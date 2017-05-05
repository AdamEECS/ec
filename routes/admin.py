from models.product import Product
from models.order import Order
from models.user import User
from routes import *
from flask import current_app as app
import qiniu

main = Blueprint('admin', __name__)

Model = Product
from config import key

q = qiniu.Auth(key.qiniu_access_key, key.qiniu_secret_key)


@main.route('/add')
@admin_required
def add_page():
    u = current_user()
    key = 'my-python-logo.png'
    # 上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
    policy = {
        'callbackUrl': app.config['QINIU_CALLBACK_URL'],
        'callbackBody': 'filename=$(fname)&'
                        'filesize=$(fsize)&'
                        'route=$(x:route)&'
                        'name=$(x:name)&'
                        'price=$(x:price)',
    }
    token = q.upload_token(app.config['CDN_BUCKET'], policy=policy)
    return render_template('product_add.html', u=u, token=token)


@main.route('/add', methods=['POST'])
@admin_required
def add():
    u = current_user()
    form = request.form
    status, msgs = Model.valid(form)
    if status is True:
        p = Model.new(form)
        return redirect(url_for('admin.product_edit', uuid=p.uuid))
    else:
        return render_template('product_add.html', msgs=msgs, u=u)


@main.route('/products')
@admin_required
def product_list():
    u = current_user()
    ms = Model.all()
    return render_template('product_list.html', ms=ms, u=u)


@main.route('/users')
@admin_required
def user_list():
    u = current_user()
    ms = User.all()
    return render_template('admin_user.html', ms=ms, u=u)


@main.route('/orders')
@admin_required
def order_list():
    u = current_user()
    ms = Order.all()
    ms.reverse()
    for m in ms:
        m.user = User.get(m.user_id)
        m.ct = time_str(m.ct)
    return render_template('admin_order.html', ms=ms, u=u)


@main.route('/product/<uuid>', methods=['POST', 'GET'])
@admin_required
def product_edit(uuid):
    u = current_user()
    p = Model.find_one(uuid=uuid)
    policy = {
        'callbackUrl': app.config['QINIU_CALLBACK_URL'],
        'callbackBody': 'filename=$(fname)&'
                        'filesize=$(fsize)&'
                        'route=$(x:route)&',
        'returnUrl': url_for('admin.product_edit', uuid=p.uuid),
        'mimeLimit': 'image/*',
    }
    u.token = q.upload_token(app.config['CDN_BUCKET'], key=uuid, policy=policy)
    u.upload_url = app.config['PIC_UPLOAD_URL']
    return render_template('product_edit.html', p=p, u=u)


@main.route('/update/<uuid>', methods=['POST'])
@admin_required
def product_update(uuid):
    p = Model.find_one(uuid=uuid)
    form = request.form
    # pic = request.files['pic']
    p.update(form)
    # p.update_pic(pic)
    return redirect(url_for('admin.product_edit', uuid=p.uuid))


@main.route('/delete/<int:id>')
@admin_required
def product_delete(id):
    p = Model.get(id)
    # p.delete()
    return redirect(url_for('admin.product_list'))


@main.route('/user_edit/<int:id>')
@admin_required
def user_edit(id):
    u = current_user()
    m = User.get(id)
    ps = m.get_cart_detail()
    return render_template('admin_user_edit.html', m=m, ps=ps, u=u)


@main.route('/user_delete/<int:id>')
@admin_required
def user_delete(id):
    m = User.get(id)
    # m.delete()
    return redirect(url_for('admin.user_list'))


@main.route('/user_update/<int:id>', methods=['POST'])
@admin_required
def user_update(id):
    m = User.get(id)
    form = request.form
    m.update_user(form)
    return redirect(url_for('admin.user_list'))


@main.route('/order_edit/<orderNo>')
@admin_required
def order_edit(orderNo):
    u = current_user()
    m = Order.find_one(orderNo=orderNo)
    m.user = User.get(m.user_id)
    m.ct = time_str(m.ct)
    return render_template('admin_order_edit.html', o=m, u=u)


@main.route('/order_delivery/<orderNo>')
@admin_required
def order_delivery(orderNo):
    o = Order.find_one(orderNo=orderNo)
    o.delivery()
    return redirect(url_for('admin.order_list'))


# @main.route('/root')
# @login_required
# def root_set():
#     root = User.find_one(username='root')
#     root.role = 'admin'
#     root.save()
#     return redirect(url_for('admin.product_list'))
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
#     return redirect(url_for('admin.product_list'))


@main.route('/clear_order_items')
@admin_required
def clear_order_items():
    os = Order.all()
    for o in os:
        o.items = []
        o.save()
    return redirect(url_for('admin.product_list'))


@main.route('/clear_orders')
@admin_required
def clear_orders():
    os = Order.all()
    for o in os:
        o.delete()
    return redirect(url_for('admin.product_list'))
