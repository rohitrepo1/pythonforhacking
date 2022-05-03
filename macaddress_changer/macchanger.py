# calling python module  and changing the  MAC address #
from ast import arguments
from email import parser
import subprocess
import optparse
from pandas import options

from macchanger_function import *
#parser = optparse.OptionParser()
#parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
#parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
#(options, arguments) = parser.parse_args()
#(options, arguments) = get_arguments()
options = get_arguments()
#interface = options.interface
#new_mac = options.new_mac
change_mac(options.interface, options.new_mac)
#subprocess.call(["ifconfig", interface, "down"])
#subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#subprocess.call(["ifconfig", interface, "up"])
print("the new mac address is:",options.new_mac)

