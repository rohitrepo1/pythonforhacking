# calling python module  and changing the  MAC address #
from ast import arguments
from email import parser
import subprocess
import optparse
from pandas import options
from macchanger_function import *
(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
print("the new mac address is:",options.new_mac)