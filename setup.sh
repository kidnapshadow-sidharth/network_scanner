#!/bin/bash

clear

#define color 
red='\e[1;31m'
green='\e[1;32m'
blue='\e[1;34m'
blink='\e[5m'
stop_blink='\e[25m'
stop_color='\e[0m'


echo -e "$red**********************************************************************$stop_color"
echo -e  """ $green  

.-----.-----.|  |_.--.--.--.-----.----.|  |--.-----.----.---.-.-----.-----.-----.----.
|     |  -__||   _|  |  |  |  _  |   _||    <|__ --|  __|  _  |     |     |  -__|   _|
|__|__|_____||____|________|_____|__|  |__|__|_____|____|___._|__|__|__|__|_____|__|  
                                                                                      
------------------------------------------------------------------------------------
                                                        Crafted by sidharth
                                                        Twitter: kidnapshadow_kd
------------------------------------------------------------------------------------
 $stop_color """

echo -e "$red**********************************************************************$stop_color"


echo -e "Getting Things Ready For You..... :) \n"

apt-get install python3

apt-get install python3-pip

pip3 install scapy.all

pip3 install sys

pip3 install colorama

chmod +x network_scanner.py

cp network_scanner.py /usr/bin/network_scanner.py

echo -e "\ndone...\n"

clear

python3 network_scanner.py 127.0.0.1