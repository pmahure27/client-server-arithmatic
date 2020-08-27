import socket			 

s = socket.socket()		 
port = 33333
s.connect(('127.0.0.1', port)) 

a,b = '20','5'
# a,b = input("enter space separated 2 inputs :").split()
data = a+' '+b

size = s.send(data.encode())
print("Size : ",size)
data = s.recv(19).decode()
result = data.split()

print("Addition       = ",result[0]) 
print("Substraction   = ",result[1]) 
print("Multiplication = ",result[2]) 
print("Division       = ",result[3]) 

s.close()