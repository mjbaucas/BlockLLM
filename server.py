import socket
import time
import sys
from langchain_community.llms import Ollama

ip_addresses = [
    "10.12.232.205",
   # "10.12.210.205", 
   # "10.12.168.114",
   # "10.12.208.45",
   # "10.12.240.116",
   # "10.12.128.65",
   # "10.12.195.251",
   # "10.12.141.136",
   # "10.12.191.219",
   # "10.12.204.225"
]

llm = Ollama(
    model="granite3.2:2b",
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