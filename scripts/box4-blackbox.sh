sed -i "s/#Port 22/Port 5555/" /etc/ssh/sshd_config
service ssh restart 
IP=$(shuf -i 20-250 -n 1)
ip a d 192.168.30.3/24 dev eth0
ip a a 192.168.30.$IP/24 dev eth0
echo BOX3 > /proc/sys/kernel/hostname

