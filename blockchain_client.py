import socket
import time 
import sys
from blockchain.public import Chain as PublicBlockchain

pub_chain = PublicBlockchain(4)
mode = sys.argv[1]

reset = 1
start = 0
while True:
	if reset == 1:
		start = time.time()
		reset = 0
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("10.12.200.169", 5000))
		if mode == 0:
			s.sendall(bytes('default', "utf-8"))
			message = s.recv(1024).decode("utf-8")            
		else:
			proof = pub_chain.proof_of_work(pub_chain.gen_block)
			s.sendall(bytes(proof, "utf-8"))
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