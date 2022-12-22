#!/bin/bash

# Initial setup
setup() {
sudo apt-get -y install terminator docker docker-compose
sudo docker pull debian:buster
sudo docker build -t labimage .
}


# Create containers
create() {
sudo docker container list | grep sshdocker && sudo docker-compose down --remove-orphans
sudo docker-compose up -d
sudo docker container list
}

# Drop to shell on box 1
box1() {
sudo docker exec --privileged -it sshdockerlab-main_container1_1 /bin/bash
}

setup
create
box1


