__author__ = 'sam'
"""
Sample code to learn socket programming in python through socket module use.
Here we are opening a port and receving on it.
Clients can connect to the port to have communication.
"""
import socket               # Import socket module
s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '' 
port = 12345 				# Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for mac 5client connection.
while True:
    connection, addr = s.accept()     # Establish connection with client.
    #listening started
    print 'Got connection from', addr
    connection.send('Thank you for connecting')
    try:
        print 'connection from', addr
            # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1)
            print 'SERVER : received "%s"' % data
            if data:
                print 'SERVER: sending data back to the client'
                connection.sendall(data)
            else:
                print 'SERVER: no more data from', addr
                break
    finally:
            # Clean up the connection
            connection.close()

