from routes import *
from flask import current_app as app

import qiniu
from config import key

q = qiniu.Auth(key.qiniu_access_key, key.qiniu_secret_key)

main = Blueprint('callback', __name__)


@main.route('/all', methods=['POST'])
def product_add():
    body = request.get_data()
    body = body.decode('utf-8')
    form = request.form
    auth = request.headers.get('Authorization')
    url = app.config['QINIU_CALLBACK_URL']
    print(form)
    verify = q.verify_callback(auth, url, body)
    if verify:
        print('verify :', verify)
    r = {"success": True}
    return json.dumps(r)
