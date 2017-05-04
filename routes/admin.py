from models.product import Product
from models.order import Order
from models.user import User
from routes import *
from flask import current_app as app

main = Blueprint('admin', __name__)

Model = Product


@main.route('/add')
@admin_required
def add_page():
    u = current_user()
    return render_template('product_add.html', u=u)


@main.route('/add', methods=['POST'])
@admin_required
def add():
    u = current_user()
    form = request.form
    pic = request.files['pic']
    status, msgs = Model.valid(form)
    print(status, msgs)
    if status is True:
        p = Model.new(form)
        p.update_pic(pic)
        msgs.append('{}创建成功'.format(p.name))
        return redirect(url_for('admin.product_list'))
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


@main.route('/edit/<int:id>')
@admin_required
def product_edit(id):
    u = current_user()
    p = Model.get(id)
    print(p)
    return render_template('product_edit.html', p=p, u=u)


@main.route('/update/<int:id>', methods=['POST'])
@admin_required
def product_update(id):
    p = Model.get(id)
    form = request.form
    pic = request.files['pic']
    p.update(form, hard=True)
    p.update_pic(pic)
    return redirect(url_for('admin.product_list'))


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