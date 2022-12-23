PASS=$(head -n 100 /mnt/rockyou.txt | shuf -n 1)
echo "user:$PASS" | chpasswd
PORT=$(shuf -i 2000-65000 -n 1)
sed -i "s/#Port 22/Port $PORT/" /etc/ssh/sshd_config
service ssh restart 
python3 -m http.server 22 &
echo CASTLE > /proc/sys/kernel/hostname
echo "FLAG" | md5sum |cut -d" " -f 1 > /home/ubuntu/flag.txt
