#!/bin/bash -e

sudo yum -y install gcc-c++ make
curl -sL https://rpm.nodesource.com/setup_10.x | sudo -E bash -
sudo yum -y install nodejs
