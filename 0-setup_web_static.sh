#!/usr/bin/env bash
# Install Nginx if it not already installed
# Create the folder /data/web_static/shared/
# Create the folder /data/web_static/releases/test/
# Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
# Create a symbolic link /data/web_static/current linked
# to the /data/web_static/releases/test/ folder
# Give ownership of the /data/ folder to the ubuntu user AND group
#Update the Nginx configuration to serve content of /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static).
# Don't forget to restart Nginx after updating the configuration:
# Use alias inside your Nginx configuration

html_content="<html>
<head>
</head>
<body>
        <h1>ALX Africa is the best</h1>
</body>
</html>"

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i -e "/^\s*location \/ {/a \
        location \/hbnb_static\/ {\
                alias \/data\/web_static\/current\/;\
        }" /etc/nginx/sites-available/default
sudo service nginx restart
