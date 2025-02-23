import socket
import threading

#connect tot the server
username = input("ENter your username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' #localhsot
port = 55556 #port no
client.connect((host, port))


#receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured. Disconnecting tfro tthe server....")
            client.close()
            break

#send message to the server
def write():
    while True:
        message = f"{username}: {input('message')}"
        client.send(message.encode('utf-8'))

#start receivig and sending messages simultaneuosly
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()