import socket			 

s = socket.socket()		 
port = 33333
s.bind(('127.0.0.1', port))		 
s.listen(5)	 
print ("listening..."	)
result = ''
while True: 
	c, addr = s.accept()	 
	print ('Got connection from', addr) 
	data = c.recv(10).decode()
	# print(data)
	
	a,b = data.split()
	result += str(float(a)+float(b))+' '
	result += str(float(a)-float(b))+' '
	result += str(float(a)*float(b))+' '
	result += str(float(a)/float(b))+''
	# print(result)
	size = c.send(result.encode())
	result = ''
	print("Bytes sent :", size)
	c.close()