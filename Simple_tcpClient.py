from socket import *
from random import randint
from cesar_cipher import CesarCipher

cs = CesarCipher(3)

serverName = "10.1.70.16"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = cs.cript(input("Input lowercase sentence: "))

clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = cs.decript(str(clientSocket.recv(65000), "utf-8"))

print ("Received from Make Upper Case Server: ", modifiedSentence)
clientSocket.close()