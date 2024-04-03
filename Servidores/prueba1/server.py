import socket as sk
import threading as th

HOST = "127.0.0.1"
PORT = 8000

server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()
print(F"Server Iniciado: {HOST}, {PORT}")

clients = []
usernames = []

def broadcast(message, self): #Transmision en ingles
    for client in clients:
        if client != self:
            client.send(message)

def handleMessage(client: sk.socket):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            broadcast(F"{usernames[index]} ha abandonado el chat".encode("utf-8"), client)
            clients.remove(client)
            usernames.remove(usernames[index])
            client.close()
            break

def recieveConections():
    while True:
        client, adress = server.accept()

        client.send(f"/U Usuario{len(usernames)}".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")

        clients.append(client)
        usernames.append(username)

        print(f"Se conecto {username} de direccion {adress}")

        message = f"El usuario {username} se ha unido al chat.".encode("utf-8")
        broadcast(message, client)
        client.send(b"Conectado al servidor")

        thread = th.Thread(target=handleMessage, args=(client,))
        thread.start()

recieveConections()