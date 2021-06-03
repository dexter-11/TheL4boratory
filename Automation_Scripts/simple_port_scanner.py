#!/usr/bin/python3

import sys
import socket
from datatime import datetime

## Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #Translate hostname to IPv4
else
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")
    
#Add a pretty banner
print("-" * 50)
print("Scanning Target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scoket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))   #returns an error indicator
        if result == 0:
                print("Port {} is open", format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\n Exiting program!")
    sys.exit()  

except socket.gaierror:
    print("\n Hostname couldn't be resolved.")
    sys.exit()  

except socket.error:
    print("\n Couldn't connect to server!")
    sys.exit()  
