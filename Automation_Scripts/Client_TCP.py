#!/usr/bin/python
import socket

target_host = '127.0.0.1'
target_port = 9091

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send any data
client.send(b"Ohh LOL you found me!")

# Receive response
response = client.recv(4096)

print(response.decode())
client.close()
