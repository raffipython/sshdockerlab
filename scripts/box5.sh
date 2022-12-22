sed -i "s/#Port 22/Port 5555/" /etc/ssh/sshd_config
service ssh restart 
python3 -m http.server 22 &
echo CASTLE > /proc/sys/kernel/hostname
echo "FLAG" | md5sum |cut -d" " -f 1 > /home/ubuntu/flag.txt
