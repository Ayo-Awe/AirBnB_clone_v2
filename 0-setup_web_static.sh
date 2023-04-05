#!/usr/bin/env bash
# Sets up web servers for web static deployment

apt-get update -y
apt-get install -y nginx
mkdir -p  /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello World" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu -R /data/
echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        add_header X-Served-By \$hostname always;

        error_page 404 /404.html;
        location /404.html {
                 root /usr/share/nginx/html;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        location /hbnb_static/ {
				alias /data/web_static/current;
        }

        location / {
                try_files \$uri \$uri/ =404;
        }
}" > /etc/nginx/sites-enabled/default
service nginx restart
