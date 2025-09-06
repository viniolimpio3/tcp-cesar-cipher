from socket import *
from random import randint
from cesar_cipher import CesarCipher
from DiffieHellman import DiffieHellman


n = 100000007  # número primo
g = 5   # base
df = DiffieHellman(n, g)

# Gera chaves Diffie-Hellman
r  = df.implement()

serverName = "10.1.70.16"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Envia chave pública do cliente
clientSocket.send(str(r).encode('utf-8'))

# Recebe chave pública do servidor
server_x = int(clientSocket.recv(1024).decode('utf-8'))

# Computa chave compartilhada
shared_key = df.compute_shared_key(other_x=server_x)

cs = CesarCipher()

sentence = cs.cript(input("Input lowercase sentence: "))

clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = cs.decript(str(clientSocket.recv(65000), "utf-8"))

print ("Received from Make Upper Case Server: ", modifiedSentence)
clientSocket.close()