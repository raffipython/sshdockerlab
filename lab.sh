#!/bin/bash

# Initial setup
sudo apt-get -y install terminator docker docker-compose
sudo docker pull debian:buster
sudo docker images |grep buster
sudo docker build -t labimage .
sudo docker images |grep labimage

# Create containers
sudo docker container list | grep lab_ && sudo docker-compose down --remove-orphans
sudo docker-compose up -d
sudo docker container list

# Drop to shell on box 1
sudo docker exec --privileged -it sshdockerlab-main_container1_1 /bin/bash

