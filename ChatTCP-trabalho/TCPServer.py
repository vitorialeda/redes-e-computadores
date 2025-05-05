from socket import *
from _thread import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", 12000))
serverSocket.listen(5)
print(f"Server rodando na porta {serverPort}")


def handleCliente(connectionSocket, addr):
    print(f"O cliente {addr} se conectou.")
    while True:
        mensagemRecebida = connectionSocket.recv(1024).decode("utf-8")
        print(mensagemRecebida)

    #TO DO: enviar mensagem de volta


while True:
    connectionSocket, addr = serverSocket.accept()

    thread = threading.Thread(target= handleCliente, args=(connectionSocket, addr))
    thread.daemon = True
    thread.start()

    mensagem = connectionSocket.recv(1024).decode("utf8")
    print(f"{addr}: {mensagem}")
    
serverSocket.close()