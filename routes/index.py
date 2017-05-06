from . import *
from models.product import Product
from flask import current_app as app

main = Blueprint('index', __name__)


@main.route('/')
def index():
    u = current_user()
    ps = Product.all()
    return render_template('front.html', u=u, ps=ps)


@main.route('/', methods=['POST'])
def index_search():
    u = current_user()
    search = request.form.get('search', None)
    if search:
        ps = Product.find(name={'$regex': search, '$options': '$i'})
        return render_template('index.html', u=u, ps=ps)
    else:
        return redirect(url_for('index.index'))
