import socket
import time 

reset = 1
start = 0
while True:
	if reset == 1:
		start = time.time()
		reset = 0
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("10.12.200.169", 5000))
		s.sendall(bytes('Are antibiotics effective on viral infections?', "utf-8"))
		message = s.recv(1024).decode("utf-8")
		if message  != "":
			end = time.time()
			elapsed = end-start
			if elapsed > 1.0:
				print(elapsed)
			reset = 1
		else:
			reset = 0
		s.close()
	except Exception as msg:
		print(msg)
		reset = 0
