from socket import *

ip="127.9.8.98"
port=30197

clientsocket=socket(AF_INET, SOCK_DGRAM)
no=raw_input("Enter alphabets to be sorted: ")
clientsocket.sendto(no,(ip,port))
newno, addr=clientsocket.recvfrom(2048)
print "Sorted alphabets(from server): ",newno
print 
clientsocket.close()
