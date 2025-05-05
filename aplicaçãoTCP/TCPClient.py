from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM representa o tipo de socket "TCP"
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase sentence:")

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print("From server: ", modifiedSentence)

clientSocket.close()