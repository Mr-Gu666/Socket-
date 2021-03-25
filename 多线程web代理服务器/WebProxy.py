from socket import *

buffsize = 1024

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('',5670))
tcpSerSock.listen(5)

while 1:
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	message = tcpCliSock.recv(buffsize).decode()
	filename = message.split()[1].partition("//")[2].replace('/', '_')
	if filename=="":
		continue
	fileExist = "false"
	filetouse = "/" + filename
	print("filename is: "+filename)
	try:
		f = open(filetouse[1:], "r")
		outputdata = f.read()
		fileExist = "true"
		tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
		tcpCliSock.send("Content-Type:text/html\r\n".encode())
		tcpCliSock.sendall(outputdata.encode())
		print('Read from cache')
	except IOError:
		if fileExist == "false":
			c = socket(AF_INET,SOCK_STREAM)
			hostn = message.split()[1].partition("//")[2].split("/")[0]
			print("hostn = "+hostn)
			try:
				c.connect((hostn,80))
				c.send(message.encode())
				buf = c.recv(65536)
				tcpCliSock.sendall(buf)
				tmpFile = open("./" + filename,"w")
				tmpFile.writelines(buf.decode().replace('\r\n','\n'))
				tmpFile.close()
			except:
				print("Illegal request")
			c.close()
		else:
			print('Not found file')
	print("tcpCliSock closed")
	tcpCliSock.close()
tcpSerSock.close()