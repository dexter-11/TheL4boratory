#!/bin/bash
if [ "$1" == "" ]
    echo "You forgot IP address! Sample execution --> ./ipsweep.h 192.168.2"   
else
    for ip in `seq 1 254` ; do
        ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &  
        # ['&' allows threading else it would go one IP at a time]
    done
fi
