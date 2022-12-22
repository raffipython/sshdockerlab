service ssh start 
echo BOX2 > /proc/sys/kernel/hostname
echo "HELLO TO BOX 2 " > index.html
python3 http.server 8000 &
