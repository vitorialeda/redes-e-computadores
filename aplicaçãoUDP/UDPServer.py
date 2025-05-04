from socket import *

# Define número da porta do servidor
serverPort = 1200

# Cria socket do server
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Vincula o numero 1200 ao socket do server // Não cria automaticamente como fizemos no UDPClient.py
# O "" é o espaço para colocar o nome de hospedeiro
serverSocket.bind(("", serverPort))

# Indicativo visual de que o server está rodando
print("The server is ready to recieve")

while True:
    # =-=-=-=-= Recebimento =-=-=-=-=-
    # Recebe a mensagem e o endereço do cliente e armazena nas respectivas variáveis
    message, clientAddress = serverSocket.recvfrom(2040)

    # =-=-=-=- Processamento -=-=-=-=-
    # Converte a mensagem de byte pra string e então a modifica
    modifiedMessage = message.decode().upper()

    # =-=-=-=-=-=- Envio =-=-=-=-=-=-
    # Converte a mensagem codificade de string para byte e envia para o cliente pelo socket do servidor 
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

    # OBS:
    # - O endereço do servidor tambem está conectado ao pacote enviado