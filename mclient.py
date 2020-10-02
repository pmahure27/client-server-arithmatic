import socket 
import sys
import threading

server = socket.gethostname()
port = 9696
def rec(sck):
	data = sck.recv(1024)
	while data:
		if data.decode() == '-----end-----':
			break
		print(data.decode())
		data = sck.recv(1024)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
	try:
		sck.connect((server, port))
	except Exception as e:
		raise SystemExit(f"Can't connect to {server}:{port}, because: {e}")

	while True:
		msg = input("Space separated 2 numbers ('e' to exit): ")
		if msg =='e':
			sck.sendall(msg.encode('utf-8'))
			print("Client is saying goodbye!")
			sys.exit()
		sck.sendall(msg.encode('utf-8'))
		threading._start_new_thread(rec,(sck,))