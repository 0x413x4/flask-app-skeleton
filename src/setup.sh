#!/bin/bash

echo '=================================================='
echo '=                Project Mongoose                ='
echo '=================================================='
echo 'Start provisioning...'

# Set hostname
hostnamectl set-hostname the-den

cat >/etc/hosts <<EOL
127.0.0.1       localhost
127.0.1.1       the-den

ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
EOL

cd /app-skeleton

# Install dependencies
apt-get update
< os-requirements.txt xargs apt-get install -y

# Install python dependencies
pip3 install -r requirements.txt

# Intialise database
flask db init
flask db migrate
flask db upgrade

# Install tools
# TODO

# Setup services
# TODO

# Start services
# TODO
