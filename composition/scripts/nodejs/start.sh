#!/bin/bash -e

sudo mkdir -p /var/run/nodejs
sudo chmod 777 /var/run/nodejs
nohup node ~/server.js > /dev/null 2>&1 &
