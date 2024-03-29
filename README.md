# sshdockerlab

![image](https://user-images.githubusercontent.com/29049788/209403469-f023e5db-cf38-4af5-96dd-b998adabe281.png)

**Initial Setup (IF YOU GOT HERE FOR TRAINING, PLEASE RUN THE SETUP AND INSTALL LAB FILES WHILE YOU HAVE INTERNET SINCE CLASSROOM DOESNT HAVE WIFI, YOU MIGHT NEED TO APT UPDATE FIRST IF DOCKER IS NOT INSTALLED) **

`cd ~/Downloads`

`unzip sshdockerlab-main.zip ; cd sshdockerlab-main`

Make sure you have python3 installed

`python3 -V`

Download and install lab files (need sudo, it may prompt you for your password)

`chmod +x ./sshdockerlab.py ; ./sshdockerlab.py -i`


**Create lab containers**

Default creds for the boxes are user:password but for blackbox and insane versions passwords are random. There are three modes for this lab:

***classic*** *[default five box setup]*

***blackbox*** *[port and password are random]*

***insane*** *[similar to classic but with extra boxes and multi-nic boxes]*

`./sshdockerlab.py -c` , `./sshdockerlab.py -c -t blackbox` , or `./sshdockerlab.py -c -t insane` (need sudo, it may prompt you for your password)


**Interacting with lab containers**

First box is PENTESTER box that you will use to start with. If you are using Kali and want to use your host as first box you can. Your host IP should be 192.168.10.1 so you can SSH to 192.168.10.2 in the beginning.

To list containers for debugging purposes:

`./sshdockerlab.py -l` (need sudo, it may prompt you for your password)

To get shell on first box:

`./sshdockerlab.py -s 1` (need sudo, it may prompt you for your password)

You can use other box numbers such as 2 in the command above to get direct shell to the other boxes. However, this should be used only for debugging purposes. Only get a shell on the first box and walk your way out.

**Ending lab**

To end the lab and destroy all containers:

`./sshdockerlab.py -e` (need sudo, it may prompt you for your password)

**Notes**
Docker commands can be senstive to the current working directory. Make sure you are in *sshdockerlab-main* folder when running the `sshdockerlab.py` commands. 

Use `hydra` and `nmap`. /mnt/ is mounted locally so you can use /mnt/rockyou.txt when bruteforcing.

For ssh tunneling probably a good idea to use -fNT flags so you keep your current shell on the PENTESTER box for example:

`ssh -fNT -L 127.0.0.1:9999:TGT_TWO:TGT_PORT USER@TGT_ONE`

Lab layout of classic and blackbox mode:

*BOX1 -> BOX2 -> BOX3 -> BOX4 -> BOX5*

IP of BOX1 is 192.168.10.2. BOX2 is 192.168.10.3 (or random one in blackbox mode). There are four subnets and your goal is to reach BOX5

Lab layout of insane:

*BOX1 -> BOX2 -> BOX3 -> BOX4 -> BOX5 -> BOX6 -> BOX7*

*BOX6 -> BOX8*

*BOX6 -> BOX9 -> BOX10*


**Customizing your build**

To edit the base image and add extra packages, edit the Dockerfile and rerun `./sshdockerlab.py -i`

To edit the network map pass your custom docker-compose yaml file to the main script for example 

`./sshdockerlab.py -c -t docker-template.yml`

To edit a box setup, modify/create a bash script such as box1.sh and pass that to the docker-compose yaml file in the command section for example 

*command: /bin/bash -c "bash /mnt/scripts/BOXNAME.sh;while true; do echo 'alive' && sleep 60; done"*

