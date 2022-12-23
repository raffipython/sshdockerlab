FROM debian:buster

RUN apt update && apt install openssh-server sudo net-tools netcat python3 vim iptables wget curl nmap hydra -y

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 user 

RUN echo 'user:password' | chpasswd

