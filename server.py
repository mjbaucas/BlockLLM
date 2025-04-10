import socket
import time
import sys
from langchain_community.llms import Ollama

ip_addresses = [
    "10.12.205.237",
    "10.12.195.88",
    "10.12.172.181",
    "10.12.232.205",
    "10.12.213.45",
    "10.12.243.189",
    "10.12.208.85",
    "10.12.131.80" #,
    #"10.12.191.219",
    #"10.12.141.20"
]

llm = Ollama(
    model="hf.co/FreedomIntelligence/Apollo-6B-GGUF",
)

def get_llm_response(prompt):
    output = llm.invoke(prompt)
    return output


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
        print(message)
        response = get_llm_response(message.decode("utf-8"))
        connection.sendall(bytes(response, "utf-8"))
        counter+=1
        if counter >= len(ip_addresses):
            counter = 0
    else:
        connection.recv(1024)
        connection.sendall(bytes("", "utf-8"))
        
    print(counter)
    connection.close()