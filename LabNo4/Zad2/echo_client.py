# -- coding: utf-8 --
import socket
host = socket.gethostname()
port = 12345
client_socket = socket.socket()     # TCP socket

client_socket.connect((host,port))

client_socket.sendall('Tekst koji se salje serveru')

data = client_socket.recv(1024)     # Tekst koji je primljen od servera

print (data)                        # Ispis podataka

client_socket.close()               # Close the connection

