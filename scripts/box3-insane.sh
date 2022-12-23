PASS=$(head -n 100 /mnt/rockyou.txt | shuf -n 1)
echo "user:$PASS" | chpasswd
PORT=$(shuf -i 2000-65000 -n 1)
sed -i "s/#Port 22/Port $PORT/" /etc/ssh/sshd_config
service ssh start 
echo BOX2 > /proc/sys/kernel/hostname
echo "HELLO TO BOX 2 " > index.html
python3 http.server 8000 &
