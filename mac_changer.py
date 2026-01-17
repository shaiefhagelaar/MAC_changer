#!/usr/bin/env python

import subprocess

#Turns off eth0
subprocess.call(["ifconfig eth0 down"], shell=True)

#Writes new mac address
subprocess.call(["ifconfig eth0 down hw ether 00:11:22:33:44:15"], shell=True)

#Turns on eth0
subprocess.call(["ifconfig eth0 up"], shell=True)

#Displays new mac address
subprocess.call(["ifconfig | grep eth0"], shell=True)
