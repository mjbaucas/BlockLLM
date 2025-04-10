import socket
import time
import sys
from blockchain.private import Chain as PrivateBlockchain
from blockchain.public import Chain as PublicBlockchain

ip_addresses = [
    "10.12.205.237",
    #"10.12.195.88"
    #"10.12.172.181",
    #"10.12.232.205",
    #"10.12.213.45",
    #"10.12.243.189",
    #"10.12.208.85",
    #"10.12.131.80",
    #"10.12.191.219",
    #"10.12.141.20",
]

#intialize private blockchain
trusted_list = ip_addresses.copy()
trusted_list.append("default")

priv_chain = PrivateBlockchain()
priv_chain.gen_next_block("0", trusted_list)

#initialize public blockchain
pub_chain = PublicBlockchain(4)

mode = sys.argv[1]

counter = 0
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5000))
    s.listen(5)
    print('Server is now running.')
    connection, address = s.accept()
    print(address)
    if address[0] == ip_addresses[counter]:
        print(f"Connection from {address} has been established.")
        message = connection.recv(1024)
        print(message.decode("utf-8"))
        response =""
        if mode == "0":
            if priv_chain.search_ledger(message.decode("utf-8")):
                response = "access granted"
            else:
                response = "access rejected"
        elif mode == "1":
            if pub_chain.verify_proof(pub_chain.gen_block, message.decode("utf-8")):
                response = "access granted"
            else:
                response = "access rejected"
        connection.sendall(bytes(response, "utf-8"))
        counter+=1
        if counter >= len(ip_addresses):
            counter = 0
    else:
        connection.shutdown(socket.SHUT_RDWR)
        connection.close()
        
    print(counter)
    connection.close()