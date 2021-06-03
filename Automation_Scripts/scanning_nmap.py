#!/usr/bin/python3

import nmap
import sys

nm_scan = nmap.PortScanner()
print("\n Running....\n")
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments="-O")      # sys.argv[1] because IP is the first argument we provide here

pprint(nm_scanner)   # print a dictionary using the pprint library

print("The host is "+nm_scanner['scan']['127.0.0.1']['status']['state'])               # recursive filtering of results
print("The port 80 is "+nm_scanner['scan']['127.0.0.1']['tcp'][80]['state']) 
print("The scanning method is "+nm_scanner['scan']['127.0.0.1']['tcp'][80]['reason']) 

print("There is %s percent chanes that the host is running %s"%(nm_scanner['scan']['127.0.0.1']['osmatch'][0]['accuracy'],nm_scanner['scan']['127.0.0.1']['osmatch'][0]['name']))


#We can also store all these results in certain variables and print them in a file
host_status = "The host is "+nm_scanner['scan']['127.0.0.1']['status']['state']+".\n"
port_status = "The port 80 is "+nm_scanner['scan']['127.0.0.1']['tcp'][80]['state']+".\n"
method_scan = "The scanning method is "+nm_scanner['scan']['127.0.0.1']['tcp'][80]['reason']+".\n" 
os_guess = "There is %s percent chanes that the host is running %s"%(nm_scanner['scan']['127.0.0.1']['osmatch'][0]['accuracy'],nm_scanner['scan']['127.0.0.1']['osmatch'][0]['name'])+".\n"

with open(%s.txt"%sys.argv[1], ‘w’) as f:
        f.write(host_status+port_status+method_scan+os_guess)
        f.write("\nReport generated “+time.strftime(%Y-%m-%d+%H:%M:%S GMT”, time.gmtime()))

print("\nFinished..!")
