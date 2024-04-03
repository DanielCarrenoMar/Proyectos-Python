import socket as sk
import threading as th

HOST = "127.0.0.1"
PORT = 8000

client = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Ingrese su nombre de usuario: ")

def receiveMessages():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "/username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("Ha ocurrido un error")
            client.close()
            break

def writeMessages():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode("utf-8"))

receiveThread = th.Thread(target=receiveMessages)
receiveThread.start()

writeThread = th.Thread(target=writeMessages)
writeThread.start()