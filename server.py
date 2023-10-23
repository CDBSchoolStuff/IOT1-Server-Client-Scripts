from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ()
print ("-------------------------------")
print ("Serveren er klar til at modtage")
print ("-------------------------------")
print ()
print ()

while True:
    message, klient = serverSocket.recvfrom(2048)
    receivedDict = message.decode()

    print(receivedDict)
    print ()