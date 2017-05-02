from models.product import Product
from models.user import User
from routes import *
from flask import current_app as app

main = Blueprint('admin', __name__)

Model = Product


@main.route('/add')
@admin_required
def add_page():
    return render_template('product_add.html')


@main.route('/add', methods=['POST'])
@admin_required
def add():
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
        return render_template('product_add.html', msgs=msgs)


@main.route('/list')
@admin_required
def product_list():
    ps = Model.all()
    return render_template('product_list.html', ps=ps)


@main.route('/edit/<int:id>')
@admin_required
def product_edit(id):
    p = Model.get(id)
    print(p)
    return render_template('product_edit.html', p=p)


@main.route('/update/<int:id>', methods=['POST'])
@admin_required
def product_update(id):
    p = Model.get(id)
    form = request.form
    pic = request.files['pic']
    p.update(form, hard=True)
    p.update_pic(pic)
    return redirect(url_for('admin.product_list'))


@main.route('/root')
@login_required
def root_set():
    root = User.find_one(username='root')
    root.role = 'admin'
    root.save()
    return redirect(url_for('admin.product_list'))