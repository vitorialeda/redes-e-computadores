from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(f"Contectado ao servidor {serverName}:{serverPort}")
print("Digite 'encerrar chat' para sair")

# TO DO
while True:
    mensagem = input()
    if mensagem.lower() == "encerrar chat":
        break
    clientSocket.send(mensagem.encode())

    mensagemRecebida = clientSocket.recv(1024)
    print(mensagemRecebida)

print("Desconectado do servidor.")
clientSocket.close()