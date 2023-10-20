from socket import *

serverName = '10.136.137.71'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

print ()
print ("-----------------------------")
print ("Klienten er klar til at sende")
print ("-----------------------------")
print ()
print ()

while True:
    message = input('Skriv noget til serveren: ')
    clientSocket.sendto(message.encode(),(serverName, serverPort))