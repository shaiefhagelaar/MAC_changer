#If you want to run it with Python 2 change input to raw_input
interface = input("Enter the interface you want to change mac address: ")
new_mac = input("Enter the new mac address: ")
print("[+] Changing MAC address " + interface + " to " + new_mac)

#Turns off eth0
subprocess.call(["ifconfig", interface, "up"])

#Writes new mac address
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

#Turns on eth0
subprocess.call(["ifconfig", interface, "up"])

#Displays new mac address
subprocess.call(["ifconfig",])
