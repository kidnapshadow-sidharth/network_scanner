import sys
from scapy.all import srp
from scapy.layers.l2 import ARP, Ether
from colorama import init, Fore

init()
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Fore.RESET

target_network = sys.argv[1]

online_client = []

ether = Ether(dst='ff:ff:ff:ff:ff:ff')
arp = ARP(pdst=target_network)
probe = ether/arp

result = srp(probe, timeout=3, verbose=0)

#[ answered ,unanswerd]
# if you want to get answered value res=result[0]
#if you get answer in received value  answer=res[1]
#answer have two value { sent, received}

answer = result[0]
for sent, received in answer:
    online_client.append({'ip': received.psrc, 'mac': received.hwsrc})


print(f'{red}[+] Available hosts: {reset}')

print(f"{red}IP \t\t\t MAC {reset}")

for client in online_client:
    print(f"{blue}{client['ip']} \t\t {client['mac']} {reset} ")

print(f"{green}End the result :) {reset}")
print(f"{green}kidnapshadow :) {reset}")

# scanning with ICMP
# disadvantage with ICMP packet it is slow to get packet


# from scapy.all import sr1
# from scapy.layers.inet import IP, ICMP
# import ipaddress

# print("Scanning with ICMP....")
#
# ip_list = [str(ip) for ip in ipaddress.IPv4Network(target_network,False)]
#
# for ip in ip_list:
#     probe = IP(dst = ip)/ICMP()
#     result = sr1(probe, timeout=3)
#     if result:
#         print("[+] {} is online".format(ip))