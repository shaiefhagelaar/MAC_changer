#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:22:33:34:15"
print("[+] Changing MAC address " + interface + " to " + new_mac)

#Turns off eth0
subprocess.call(["ifconfig " + interface + " down "], shell=True)

#Writes new mac address
subprocess.call(["ifconfig " + interface + " hw ether " + new_mac], shell=True)

#Turns on eth0
subprocess.call(["ifconfig " + interface + " up "], shell=True)

#Displays new mac address
subprocess.call(["ifconfig"], shell=True)
