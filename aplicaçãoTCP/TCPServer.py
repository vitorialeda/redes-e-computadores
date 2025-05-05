from socket import *

# Define número da porta do servidor
serverPort = 12000

# Cria socket de entrada do server
serverSocket = socket(AF_INET, SOCK_STREAM)

# Vincula o valor da variavel serverPort ao socket do server
# O "" é o espaço para colocar o nome de hospedeiro
serverSocket.bind(("", serverPort))

# Faz com que o servidor escute requisições. O parametro especifica o numero maximo de conexões em fila
serverSocket.listen(1)
print("The server is ready to recieve")

while True:
    # Cria um novo socket dedicado ao cliente que se conectou
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    
    connectionSocket.close()