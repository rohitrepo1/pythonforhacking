from ast import arguments
import subprocess
import optparse

from pandas import options
def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    #return parser.parse_args()
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specity the interface, use --help for info")
    elif not options.new_mac:
        parser.error("[-] Pleae specity the mac, use --help for more details")
    return options    

