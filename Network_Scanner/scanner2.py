import scapy.all as scapy
import argparse

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Targer IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    Sucess = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
        
    client_list = []
    for element in Sucess:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_mac(result_list):
    print("IP\t\t\tMAC Address\n------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_argument()
scan_result = scan(options.target)
print_mac(scan_result)