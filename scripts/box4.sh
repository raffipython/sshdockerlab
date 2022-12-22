sed -i "s/#Port 22/Port 5555/" /etc/ssh/sshd_config
service ssh restart 
echo BOX3 > /proc/sys/kernel/hostname

