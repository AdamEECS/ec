from . import *
from models.product import Product
from flask import current_app as app

main = Blueprint('index', __name__)


@main.route('/')
def index():
    u = current_user()
    ps = Product.all()
    for p in ps:
        p.pic = '/{}{}.{}'.format(app.config['PRODUCT_PIC_DIR'], str(p.id), app.config['PRODUCT_PIC_EXT'])
    return render_template('index.html', u=u, ps=ps)
