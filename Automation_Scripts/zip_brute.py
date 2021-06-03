#!/usr/bin/python3

from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description"\nUsage: python zipbrute.py -z <zipfile.azip> -p <passwordfile.txt")
parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
parser.add_argument("-p", dest="passfile", help="Password file")

try:
        ziparchive=ZipFile(parsed_args.ziparchive)
        passfile=parsed_args.passfile
        foundpass=""
        
except:
        print(parser.description)
        exit(0)

#actual bruteforcing now
with open(passfile, "r") as f:  #read mode
        for line in f:
                password = line.strip("\n")
                password = password.encode("utf-8")     #for python3 only
                
                try:
                        foundpass = ziparchive.extractall(pwd=password)
                        if foundpass == None:
                                print("\nFound password: ",password.decode())
                except RuntimeError:
                        pass
                        
        if foundpass == ""
                print("\nPassword not found. Try a bigger password list.")
