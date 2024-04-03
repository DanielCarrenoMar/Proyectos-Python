import socket as sk
import threading as th
from time import sleep
from os import system

HOST = "127.0.0.1"
PORT = 8000

server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

clients = []
usernames = []
scores = {}

def handleMessage(client: sk.socket):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if message == "/exit":
                index = clients.index(client)
                print(f"{usernames[index]} se ha desconectado")
                clients.remove(client)
                scores.pop(usernames[index])
                usernames.remove(usernames[index])
                client.close()
                break
        except:
            index = clients.index(client)
            print(f"{usernames[index]} se ha desconectado")
            clients.remove(client)
            scores.pop(usernames[index])
            usernames.remove(usernames[index])
            client.close()
            break

        usuario = message[:5]
        score = message[5:]

        scores[usuario] = score

def recieveConections():
    while True:
        client, adress = server.accept()

        client.send(f"/U UCAB {len(usernames)}".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")

        clients.append(client)
        usernames.append(username)

        print(f"Se conecto {username} de direccion {adress}")

        client.send(b"Conectado al servidor")

        thread = th.Thread(target=handleMessage, args=(client,))
        thread.start()
        pantalla = th.Thread(target=screen)
        pantalla.start()

def screen():
    while True:
        sleep(3)
        system("cls")
        if len(scores) > 0:
            print("Puntuaciones:")
            for user in scores:
                print(f"{user}: {scores[user]}")
        else:
            print("No hay usuarios conectados.")

def main():
    server.bind((HOST, PORT))
    server.listen()
    print(F"Server Iniciado: {HOST}, {PORT}")

    recieveConections()



if __name__ == "__main__":
    main()