from routes import *
from models.user import User
from models.order import Order
from decimal import Decimal
from flask import current_app as app

main = Blueprint('user', __name__)

Model = User


@main.route('/login')
def index():
    return render_template('user/login.html')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username', '')
    captcha = form.get('captcha', '').lower()
    if captcha != session.get('captcha', 'no captcha!'):
        return redirect(url_for('user.index'))
    u = User.find_one(username=username)
    if u is not None and u.validate_login(form):
        session['uid'] = u.id
        return redirect(url_for('index.index'))
    else:
        return redirect(url_for('user.index'))


@main.route('/register')
def register_page():
    return render_template('user/register.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    captcha = form.get('captcha', '').lower()
    if captcha != session.get('captcha', 'no captcha!'):
        return redirect(url_for('user.register'))
    status, msgs = User.valid(form)
    if status is True:
        u = User.new(form)
        u.send_email_verify(u.email)
        session['uid'] = u.id
        return redirect(url_for('index.index'))  # TODO 邮件重置密码
    else:
        return redirect(url_for('user.register'))  # TODO 改为flash提示


@main.route('/forget_password')
def forget_password():
    return render_template('user/forget_password.html')


@main.route('/forget_password', methods=['POST'])
def forget_password_send():
    form = request.form
    captcha = form.get('captcha', '').lower()
    if captcha != session.get('captcha', 'no captcha!'):
        return redirect(url_for('user.forget_password'))
    User.forget_password(form)
    return redirect(url_for('user.forget_password'))


@main.route('/email_verify/<tb64>')
def email_verify(tb64):
    User.email_verify(tb64)
    return redirect(url_for('user.profile'))


@main.route('/forget_password_verify/<tb64>')
def forget_password_verify(tb64):
    if User.forget_password_verify(tb64):
        return render_template('user/reset_password.html', tb64=tb64)


@main.route('/reset_password/<tb64>', methods=['POST'])
def reset_password(tb64):
    password = request.form.get('password', '')
    if User.forget_password_verify(tb64):
        u = User.get_user_by_tb64(tb64)
        u.reset_password(password)
        session['uid'] = u.id
        return redirect(url_for('index.index'))


@main.route('/profile')
@login_required
def profile():
    cu = current_user()
    return render_template('user/profile.html', u=cu)


@main.route('/profile', methods=['POST'])
@login_required
def profile_update():
    cu = current_user()
    form = request.form
    cu.safe_update_user(form)
    return redirect(url_for('user.profile'))


@main.route('/update_email', methods=['POST'])
@login_required
def update_email():
    u = current_user()
    form = request.form
    new_email = form.get('email', '')
    captcha = form.get('captcha', '').lower()
    if captcha != session.get('captcha', 'no captcha!'):
        return json.dumps({'status': 'error', 'msg': 'captcha error'})
    if User.has(email=new_email) and User.find_one(email=new_email).uuid != u.uuid:
        return json.dumps({'status': 'error', 'msg': 'email exist'})
    if u.validate_login(form):
        u.send_email_verify(new_email)
        return redirect(url_for('user.profile'))
    else:
        return json.dumps({'status': 'error', 'msg': 'password error'})


@main.route('/uploadavatar', methods=['POST'])
@login_required
def avatar():
    u = current_user()
    avatar = request.files['avatar']
    u.update_avatar(avatar)
    return redirect(url_for('.profile'))


@main.route('/cart_add', methods=['GET'])
@login_required
def cart_add():
    u = current_user()
    product_uuid = request.args.get('product_uuid', None)
    u.cart_add(product_uuid)
    return redirect(url_for('user.cart'))


@main.route('/cart_sub', methods=['GET'])
@login_required
def cart_sub():
    u = current_user()
    product_uuid = request.args.get('product_uuid', None)
    u.cart_sub(product_uuid)
    return redirect(url_for('user.cart'))


@main.route('/cart')
@login_required
def cart():
    u = current_user()
    ps = u.get_cart_detail()
    u.count_num = u.get_cart_count()
    u.count_price = str(sum([Decimal(p.sum) for p in ps]))
    return render_template('user/cart.html', u=u, ps=ps)


@main.route('/cart_clear')
@login_required
def cart_clear():
    u = current_user()
    u.cart_clear()
    return redirect(url_for('user.cart'))


@main.route('/logout')
@login_required
def logout():
    p = session.pop('uid')
    print('logout: pop uid', p)
    return redirect(url_for('index.index'))


@main.route('/check_order')
@login_required
@cart_not_empty_required
@email_verify_required
def check_order():
    u = current_user()
    u.add = u.get_default_add()
    ps = u.get_cart_detail()
    u.count_num = u.get_cart_count()
    u.count_price = str(sum([Decimal(p.sum) for p in ps]))
    return render_template('user/check_order.html', u=u, ps=ps)


@main.route('/pay', methods=['POST'])
@login_required
@cart_not_empty_required
@email_verify_required
def pay():
    u = current_user()
    form = request.form
    u.buy(form)
    return redirect(url_for('user.orders'))


@main.route('/orders')
@login_required
def orders():
    u = current_user()
    os = u.orders()
    return render_template('user/orders.html', os=os, u=u)


@main.route('/order/<orderNo>')
@login_required
def order(orderNo):
    u = current_user()
    o = Order.find_one(orderNo=orderNo)
    if o is not None and o.user_id == u.id:
        return render_template('user/order.html', o=o, u=u)
    else:
        return redirect(url_for('user.orders'))


@main.route('/address')
@login_required
def address():
    cu = current_user()
    address_id = int(request.args.get('id', -1))
    if address_id >= 0:
        address_editing = safe_list_get(cu.add_list, address_id, None)
        if address_editing:
            address_editing['id'] = address_id
    else:
        address_editing = None
    return render_template('user/address.html', u=cu, a=address_editing)


@main.route('/address', methods=['POST'])
@login_required
def address_add():
    cu = current_user()
    form = request.form
    add = form.to_dict()
    cu.add_list.append(add)
    cu.save()
    return render_template('user/address.html', u=cu)


@main.route('/address_update/<int:id>', methods=['POST'])
@login_required
def address_update(id):
    cu = current_user()
    form = request.form
    add = form.to_dict()
    try:
        cu.add_list[id] = add
        cu.save()
    except IndexError:
        pass
    return redirect(url_for('user.address'))


@main.route('/address_default/<int:id>')
@login_required
def address_default(id):
    cu = current_user()
    cu.add_default = id
    cu.save()
    return redirect(url_for('user.address'))
