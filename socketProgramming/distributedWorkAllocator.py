__author__ = 'sam'
import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

data = sock.recv(1000)
print "RECEIVED FROM SERVER " + data

try:
    # Send command
    script,command=sys.argv
    print 'CLIENT: sending "%s"' % command
    #######################
    sock.sendall(command)
    #######################
    data = sock.recv(1000)
    print "RECEIVED FROM SERVER : COMMAND EXECUTION DATA -> " + data


finally:
    print 'CLIENT: closing socket'
    sock.close()