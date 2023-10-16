#!/usr/bin/python3


#import os module
import os

# It executes 'whoami' and print 
whoami_info = os.system("whoami")
print(whoami_info)

# It executes 'ip a' and print
ip_info = os.system("ip a")
print(ip_info)

# It executes 'lshw -short' and print
hardware_info = os.system("lshw -short")
print(hardware_info)
