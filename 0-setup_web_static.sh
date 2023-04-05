#!/usr/bin/env bash
# Sets up web servers for web static deployment

apt-get update -y
apt-get install -y nginx
mkdir -p  /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu -R /data/
newlines="server_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "s~server_name _;~$newlines~" /etc/nginx/sites-enabled/default
service nginx restart
