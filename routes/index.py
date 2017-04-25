from . import *
from models.product import Product

main = Blueprint('index', __name__)


@main.route('/')
def index():
    # ms = Product.all()
    u = current_user()
    # print('user:', u)
    ps = Product.all()
    return render_template('index.html', u=u, ps=ps)



