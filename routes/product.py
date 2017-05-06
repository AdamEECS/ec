from . import *
from models.user import User
from models.product import Product

main = Blueprint('product', __name__)


@main.route('/detail/<uuid>')
def detail(uuid):
    u = current_user()
    p = Product.find_one(uuid=uuid)

    return render_template('product_detail.html', p=p, u=u)
