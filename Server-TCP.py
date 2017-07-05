from socket import *

ip="127.9.8.098"
port=14995

serversocket=socket(AF_INET , SOCK_STREAM)
serversocket.bind((ip,port))
serversocket.listen(1)
while (1):
	con , addr = serversocket.accept()
	no=con.recv(2048)
	print "From client: ", no
	l=no.split(" ")
	for i in range(len(l)):
		l[i]=int(l[i])
	l.sort()
	i=1
	while(i<len(l)):
		l.insert(i,' ')
		i=i+2
	for i in range(len(l)):
		l[i]=str(l[i])
	l.reverse()
	sortedno="".join(l)
	print "Numbers to send to client: ", sortedno
	print 
	con.send(sortedno)
	con.close()
