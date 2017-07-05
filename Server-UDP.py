from socket import *

ip="127.9.8.98"
port=30197

serversocket=socket(AF_INET,SOCK_DGRAM)
serversocket.bind((ip,port))
while(1):
	no , clientaddr=serversocket.recvfrom(2048)
	print "From client: ", no
	l=no.split(" ")
	l.sort()
	i=1
	while(i<len(l)):
		l.insert(i,' ')
		i=i+2
	sortedno="".join(l)
	print "Alphabets to send to client: ", sortedno
	serversocket.sendto(sortedno,clientaddr)
