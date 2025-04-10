from blockchain.private import Chain as PrivateBlockchain
from blockchain.public import Chain as PublicBlockchain

#intialize private blockchain
trusted_list = [
    "10.12.205.237",
    "10.12.195.88",
    "10.12.172.181",
    "10.12.232.205",
    "10.12.213.45",
    "10.12.243.189",
    "10.12.208.85",
    "10.12.131.80",
    "10.12.191.219",
    "10.12.141.20",
    "default"
]

priv_chain = PrivateBlockchain()
priv_chain.gen_next_block("0", trusted_list)

#initialize public blockchain
pub_chain = PublicBlockchain(3)

proof = pchain.proof_of_work(pchain.gen_block)
print(pchain.verify_proof(pchain.gen_block, proof))

counter = 0
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5000))
    s.listen(10)
    print('Server is now running.')
    connection, address = s.accept()
    print(address)
    if address[0] == ip_addresses[counter]:
        print(f"Connection from {address} has been established.")
        message = connection.recv(1024)
        if mode == 0:
            if priv_chain.search_ledger(message.decode("utf-8")) != None
                response = "access granted"
            else 
                response = "access rejected"
        else:
            if pchain.verify_proof(pchain.gen_block, message.decode("utf-8"))
                response = "access granted"
            else 
                response = "access rejected"
        connection.sendall(bytes(response, "utf-8"))
        counter+=1
        if counter >= len(ip_addresses):
            counter = 0
    else:
        connection.recv(1024)
        connection.sendall(bytes("", "utf-8"))
        
    print(counter)
    connection.close()