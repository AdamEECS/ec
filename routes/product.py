from . import *
from models.user import User
from models.product import Product

main = Blueprint('reaction', __name__)


def current_user():
    uid = int(session.get('uid', -1))
    u = User.query.get(uid)
    return u
