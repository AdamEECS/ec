from models.user import User
from models.product import Product
from routes import *
from flask import current_app as app
from decimal import Decimal

main = Blueprint('user', __name__)

Model = User


@main.route('/login')
def index():
    return render_template('login.html')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username', '')
    u = User.find_one(username=username)
    if u is not None and u.validate_login(form):
        session['uid'] = u.id
        return redirect(url_for('index.index'))
    else:
        return redirect(url_for('.index'))


@main.route('/register')
def register_page():
    return render_template('register.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    status, msgs = User.valid(form)
    print(status, msgs)
    if status is True:
        u = User.new(form)
        session['uid'] = u.id
        return redirect(url_for('index.index'))
    else:
        return render_template('login.html', msgs=msgs)


@main.route('/profile')
@login_required
def profile():
    cu = current_user()
    cu.avatar = '/' + app.config['USER_AVATARS_DIR'] + cu.avatar
    return render_template('user_profile.html', cu=cu)


@main.route('/uploadavatar', methods=['POST'])
@login_required
def avatar():
    u = current_user()
    avatar = request.files['avatar']
    u.update_avatar(avatar)
    return redirect(url_for('.profile'))


@main.route('/nickname', methods=['POST'])
@login_required
def nickname():
    u = current_user()
    nickname = request.form['nickname']
    u.update_dict(nickname=nickname)
    return redirect(url_for('.profile'))


@main.route('/password', methods=['POST'])
@login_required
def password():
    u = current_user()
    password = request.form['password']
    u.update_dict(password=password)
    return redirect(url_for('.profile'))


@main.route('/cart_add', methods=['GET'])
@login_required
def cart_add():
    u = current_user()
    product_id = request.args.get('product_id', None)
    if product_id:
        count = u.cart.get(product_id, 0)
        count += 1
        u.cart[product_id] = count
        u.save()
    return redirect(url_for('user.cart'))


@main.route('/cart_sub', methods=['GET'])
@login_required
def cart_sub():
    u = current_user()
    product_id = request.args.get('product_id', None)
    if product_id:
        count = u.cart.get(product_id, 0)
        count -= 1
        u.cart[product_id] = count
        if count <= 0:
            u.cart.pop(product_id)
        u.save()
    return redirect(url_for('user.cart'))


@main.route('/cart')
@login_required
def cart():
    u = current_user()
    ps_id = u.cart
    ps = []
    try:
        for k, v in ps_id.items():
            p = Product.get(k)
            p.count = v
            p.sum = Decimal(p.price) * int(p.count)
            p.pic = '/{}{}.{}'.format(app.config['PRODUCT_PIC_DIR'], str(p.id), app.config['PRODUCT_PIC_EXT'])
            ps.append(p)
        u.count_num = len(ps)
        u.count_price = sum([p.sum for p in ps])
        return render_template('user_cart.html', u=u, ps=ps)
    except AttributeError:
        return redirect(url_for('user.cart_clear'))


@main.route('/cart_clear')
@login_required
def cart_clear():
    u = current_user()
    u.cart = {}
    u.save()
    return redirect(url_for('user.cart'))


@main.route('/logout')
@login_required
def logout():
    p = session.pop('uid')
    print('logout: pop uid', p)
    return redirect(url_for('index.index'))


@main.route('/check_order')
@login_required
def check_order():
    u = current_user()
    order = u.buy()
    return render_template('user_pay.html', order=order, u=u)


@main.route('/pay')
@login_required
def pay():
    u = current_user()

    return render_template('user_pay.html', u=u)


@main.route('/orders')
@login_required
def orders():
    u = current_user()
    os = u.orders()
    for o in os:
        o.ct = time_str(o.ct)
        o.name_items = []
        print('o.items', o.items)
        for k, v in o.items.items():
            p = Product.get(k)
            p.count = v
            p.pic = '/{}{}.{}'.format(app.config['PRODUCT_PIC_DIR'], str(p.id), app.config['PRODUCT_PIC_EXT'])
            o.name_items.append(p)
    return render_template('user_orders.html', os=os, u=u)
