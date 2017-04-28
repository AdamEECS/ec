ln -s /var/www/ec/config/supervisor.conf /etc/supervisor/conf.d/ec.conf

ln -s /var/www/ec/config/nginx.conf /etc/nginx/sites-enabled/ec

pip3 install -r requirements.txt