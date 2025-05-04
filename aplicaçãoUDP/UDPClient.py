from socket import *

# Dados para envio ao servidor
serverName = "hostname" # Usamos ou endereço IP ou nome de hospedeiro do servidor.

# Define número da porta do servidor
serverPort = 1200

# Cria socket do cliente
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET -> Explicita o uso de IPv4; SOCK_DGRAM -> Explicita UDP como protocolo de transporte

# Guarda mensagem digitada pelo usuário
message = input("Input lowercase sentence:")

# Envia mensagem para o servidor usando o socket do cliente
clientSocket.sendto(message.encode(),(serverName, serverPort)) # .econde() -> converte de string p byte /.sendto(data, address)

# OBS:
# - O endereço de origem tambemestá conectado ao pacote enviado
# - A porta do clientSocket é gerada automaticamente pelo SO 

# Recebe mensagem modificada e o endereço do servidor pelo socket do cliente
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # 2048 é o tamanho do buffer (esse tamanho funciona p quase todos os fins)

# Imprime mensagem recebida do servidor depois de converter de byte p string
print(modifiedMessage.decode())

# Fecha o socket
clientSocket.close()
