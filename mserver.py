import socket
import threading 
import sys
import time

host = socket.gethostname()
port = 9696
sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try: 
	sck.bind((host, port))
	sck.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")

def add(client,a,b):
	result = "\nAddition: "+str(a+b)
	client.sendall(result.encode('utf-8'))
	global last
def sub(client,a,b):
	result = "\nSubtraction: "+str(a-b)
	client.sendall(result.encode('utf-8'))
def mul(client,a,b):
	result = "\nMultiplication: "+str(a*b)
	client.sendall(result.encode('utf-8'))
def div(client,a,b):
	result = "\nDivision: "+str(a/b)
	client.sendall(result.encode('utf-8'))
def modu(client,a,b):
	result = "\nModulos: "+str(a%b)
	client.sendall(result.encode('utf-8'))
def end(client):
	time.sleep(1)
	result = '-----end-----'
	client.sendall(result.encode('utf-8'))
def on_new_client(client, connection):
	ip = connection[0]
	port = connection[1]
	print(f"{ip}:{port} Connected!")
	while True:
		msg = client.recv(1024)
		a,b=1,1
		if msg.decode() == 'e':
			break
		else:
			print(msg.decode())
			a,b = msg.decode().split()
		threading._start_new_thread(add,(client, int(a), int(b)))
		threading._start_new_thread(sub,(client, int(a), int(b)))
		threading._start_new_thread(mul,(client, int(a), int(b)))
		threading._start_new_thread(div,(client, int(a), int(b)))
		threading._start_new_thread(modu,(client, int(a), int(b)))
		threading._start_new_thread(end,(client,))
	print(f"{ip}:{port} Diconnected!")
	client.close()

while True:
	try: 
		client, ip = sck.accept()
		threading._start_new_thread(on_new_client,(client, ip))
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!")
		sck.close()
		sys.exit()
	except Exception as e:
		sck.close()
		print(f"Well I did not anticipate this: {e}")

sck.close()