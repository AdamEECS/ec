# gunicorn wsgi --worker-class=gevent -t 4 -b 0.0.0.0:8000
pip3 install -r requirements.txt
gunicorn --worker-class eventlet -w 1 wsgi
