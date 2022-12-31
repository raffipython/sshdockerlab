#!/usr/bin/env python3

# AUTHOR: raffipython

import os
import argparse

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def p(color, string):
    print(f"{color}{string}{Style.RESET_ALL}")


def banner():
    banner_string = """
         _         _            _             _       _     
 ___ ___| |__   __| | ___   ___| | _____ _ __| | __ _| |__  
/ __/ __| '_ \ / _` |/ _ \ / __| |/ / _ \ '__| |/ _` | '_ \ 
\__ \__ \ | | | (_| | (_) | (__|   <  __/ |  | | (_| | |_) |
|___/___/_| |_|\__,_|\___/ \___|_|\_\___|_|  |_|\__,_|_.__/ 
"""
    p(Fore.CYAN, banner_string)


def init():
    """ Initial setup to download files. You should only need to run this function once """
    p(Fore.YELLOW, "Downloading and installing docker, terminator, and rockyou list")
    os.system("sudo apt-get -y install terminator docker docker-compose")
    os.system("sudo docker pull debian:buster")
    os.system("sudo docker build -t labimage .")
    os.system("wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt")


def create(lab_type):
    """ Create the lab based on the type given """
    p(Fore.RED, "Removing old containers")

    # Remove old containers
    os.system("sudo docker container list | grep sshdocker && sudo docker-compose down --remove-orphans")
    
    if lab_type:
        if lab_type == "blackbox":
            dockerfilearg = "-f docker-compose-blackbox.yml"
        elif lab_type == "insane":
            dockerfilearg = "-f docker-compose-insane.yml"
        else:
            dockerfilearg = "-f " + lab_type
    else:
        dockerfilearg = ""

    # Create new containers with networking
    p(Fore.YELLOW, "Creating new containers and networks")
    os.system("sudo docker-compose " + dockerfilearg + " up -d")

    container_list()


def container_list():
    """ Lists containers """
    p(Fore.GREEN, "Containers list")
    os.system("sudo docker container list")


def container_shutdown():
    """ Shutdown the lab """
    p(Fore.RED, "Shutting down lab!\nListing containers below, there should be none.")
    os.system("sudo docker container list | grep sshdocker && sudo docker-compose down --remove-orphans")
    container_list()


def interact(box_number):
    """ Interact with a docker container """
    p(Fore.YELLOW, f"Interacting with box {box_number} via docker exec")

    # Interact with a docker container
    os.system(f"sudo docker exec --privileged -it sshdockerlab-main_container{box_number}_1 /bin/bash")


def main():
    """ Main function """
    banner()
    parser = argparse.ArgumentParser(""" SSH Docker Lab """)
    parser.add_argument("-i", "--init", action='store_true', help="Initial setup to download files. You should only need to run this function once")
    parser.add_argument("-c", "--create", action='store_true', help="Create the lab based on the type given")
    parser.add_argument("-l", "--list", action='store_true', help="List running container for debugging purposes")
    parser.add_argument("-e", "--end", action='store_true', help="End the lab and shutdown containers")
    parser.add_argument("-t", "--type", type=str, default="classic", help="Lab type: [classic (default), blackbox, insane or pass your custome docker-compose yaml file]")
    parser.add_argument("-s", "--shell", type=str, help="Box number to interact with")
    args = parser.parse_args()

    if args.init:
        init()
    elif args.create:
        create(args.type)
    elif args.shell:
        interact(args.shell)
    elif args.list:
        container_list()
    elif args.end:
        container_shutdown()
    else:
        print("Need to pass at least one argument")


main()

