#       How to Build a Chat Application in Python | Full Step-by-Step Guide
#python --version

import socket
import threading

#set up the server

host = '127.0.0.1' #localhsot
port = 55556 #port no 


#create scoket instance
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []


#broadcast messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

#handle messsages from a single client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index= clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} has left  the chat.".encode('utf-8'))
            usernames.remove(username)
            break

#receive and handle multiple clients
def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username is {username}")
        broadcast(f"{username} has joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running and listening for connections...")
receive()