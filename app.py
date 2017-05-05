from flask import Flask
from flask_script import Manager
import logging


app = Flask(__name__)
manager = Manager(app)


def register_routes(app):
    from routes.user import main as routes_user
    from routes.product import main as routes_product
    from routes.index import main as routes_index
    from routes.admin import main as routes_admin
    from routes.api import main as routes_api
    app.register_blueprint(routes_user, url_prefix='/user')
    app.register_blueprint(routes_product, url_prefix='/product')
    app.register_blueprint(routes_index, url_prefix='/')
    app.register_blueprint(routes_admin, url_prefix='/admin')
    app.register_blueprint(routes_api, url_prefix='/api')


def configure_app():

    from config import key
    app.secret_key = key.secret_key
    from config.config import config_dict
    app.config.update(config_dict)
    register_routes(app)
    # 设置 log, 否则输出会被 gunicorn 吃掉
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


if __name__ == '__main__':
    configure_app()
    manager.run()

# (gunicorn wsgi --worker-class=gevent -t 4 -b 0.0.0.0:8000 &)
