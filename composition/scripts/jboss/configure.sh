#!/bin/bash -e

sudo systemctl enable wildfly
sudo /opt/wildfly/bin/add-user.sh -u testB -p test123a