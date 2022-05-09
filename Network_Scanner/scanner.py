from socket import timeout
from numpy import broadcast
import scapy.all as scapy

#scan the network

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #print(arp_request.summary())
    #scapy.ls(scapy.ARP())
    #scapy.ls(scapy.Ether())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()
    Sucess = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    print(Sucess.summary())
    
    print("IP\t\t\tMAC Adress\n------------------------------------------------")
    for element in Sucess:
        print(element[1].psrc + "\t\t" + element[1].hwsrc )
        #print(element[1].hwsrc)
        #print("**************************************************")



scan("10.0.2.1/24")