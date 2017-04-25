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
        u.cart.append(product_id)
        u.save()
    return redirect(url_for('user.cart'))


@main.route('/cart')
@login_required
def cart():
    u = current_user()
    ps_id = u.cart
    ps = [Product.get(p) for p in ps_id]
    u.count_num = len(ps)
    u.count_price = sum([Decimal(p.price) for p in ps])
    return render_template('user_cart.html', u=u, ps=ps)


@main.route('/logout')
@login_required
def logout():
    p = session.pop('uid')
    print('logout: pop uid', p)
    return redirect(url_for('index.index'))
