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

try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    print 'CLIENT: sending "%s"' % message
    #######################
    sock.sendall(message)
    #######################

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        ####################
        data = sock.recv(1)
        ####################
        amount_received += len(data)
        print 'CLIENT: received "%s"' % data

finally:
    print 'CLIENT: closing socket'
    sock.close()