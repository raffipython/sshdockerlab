# sshdockerlab

unzip sshdockerlab-main.zip ; cd sshdockerlab-main ; chmod +x lab.sh ; ./lab.sh

CREDS:   

user:password



To get shell on a box:

sudo docker exec --privileged -it sshdockerlab-main_container<1-5>_1 /bin/bash

PENTESTER BOX for example:

sudo docker exec --privileged -it sshdockerlab-main_container1_1 /bin/bash

For ssh tunneling probably a good idea to use -fNT flags such as:

ssh -fNT -L 127.0.0.1:9999:TGT_TWO:TGT_PORT USER@TGT_ONE



