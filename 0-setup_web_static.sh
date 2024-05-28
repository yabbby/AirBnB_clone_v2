#!/bin/bash

# Update package lists
sudo apt update

# Install Nginx
if ! which nginx >/dev/null 2>&1; then
  echo "Installing Nginx..."
  sudo apt install nginx -y
fi

# Create data directory with ownership
sudo mkdir -p /data
sudo chown -R ubuntu:ubuntu /data

# Create web_static directory structure
sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir /data/web_static/releases/test

# Create a test index.html file
echo "<!DOCTYPE html><html><body><h1>Test Webpage</h1></body></html>" | sudo tee /data/web_static/releases/test/index.html

# Update symbolic link to current release
if [ -L /data/web_static/current ]; then
  echo "Removing existing current symlink..."
  sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Configure Nginx
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/hbnb_static

# Update server block configuration
sudo sed -i 's/\/var\/www\/html;/location \/hbnb_static {/g' /etc/nginx/sites-available/hbnb_static
sudo sed -i 's/index.nginx.html;  root \/var\/www\/html;/    alias \/data\/web_static\/current\/;  /g' /etc/nginx/sites-available/hbnb_static

# Enable hbnb_static site and disable default
sudo ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
sudo unlink /etc/nginx/sites-enabled/default

# Restart Nginx
echo "Restarting Nginx..."
sudo systemctl restart nginx

echo "Web server setup complete!"

