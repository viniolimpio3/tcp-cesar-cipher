from socket import *
from cesar_cipher import CesarCipher
from DiffieHellman import DiffieHellman

cs = CesarCipher(3)

# Gera chaves Diffie-Hellman
n = 100000007  # número primo
g = 5   # base
df = DiffieHellman(n, g)

x, r = df.implement()

serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()

# Recebe chave pública do cliente
client_x = int(connectionSocket.recv(1024).decode('utf-8'))

# Envia chave pública do servidor
connectionSocket.send(str(r).encode('utf-8'))

# Computa chave compartilhada
shared_key = df.compute_shared_key(other_x=client_x)

# Usa a chave compartilhada para o cifrador César
cs = CesarCipher(shared_key)

sentence = connectionSocket.recv(65000)

received = cs.decript(str(sentence,"utf-8"))
print ("Received From Client: ", received)

capitalizedSentence = cs.cript(received.upper()) # processamento

connectionSocket.send(bytes(capitalizedSentence, "utf-8"))

sent = cs.decript(capitalizedSentence)
print ("Sent back to Client: ", sent)
connectionSocket.close()