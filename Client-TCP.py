from socket import *

ip="127.9.8.098"
port=14995

clientsocket=socket(AF_INET , SOCK_STREAM)
clientsocket.connect((ip,port))

no=raw_input("Enter numbres to be sorted: ")
clientsocket.send(no)
newno=clientsocket.recv(2048)

print "Sorted numbers(from server): ",newno
clientsocket.close()
