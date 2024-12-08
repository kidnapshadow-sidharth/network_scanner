# network_scanner
This is a Network scanner tool made with python like netdiscover tool in kali linux
It can be used to scan a target or network range.

# Installation
git clone https://github.com/kidnapshadow-sidharth/network_scanner.git

cd network_scanner

sudo chmod +x setup.sh

sudo bash setup.sh

python3 network_scanner.py <ip>

# Example
python3 network_scanner.py <ip>

python3 network_scanner.py 192.168.0.0

# Requirment_for tool

import sys

from scapy.all import srp

from scapy.layers.l2 import ARP, Ether

from colorama import init, Fore

