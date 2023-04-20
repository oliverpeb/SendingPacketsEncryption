from socket import *
import ssl
serverName = "localhost"
serverPort = 12000
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
secureSocket = context.wrap_socket(clientSocket)
sentence = input('Input sentence: hej')
secureSocket.send(sentence.encode())
modifiedSentence = secureSocket.recv(1024)
print('From server: ', modifiedSentence.decode())
secureSocket.close()
