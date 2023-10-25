from socket import *
from datetime import datetime

serverName = '10.0.0.5'
serverPort = 12005
clientSocket = socket(AF_INET, SOCK_DGRAM)

print ()
print ("-------------------------------")
print ("Klar til at sende observationer")
print ("-------------------------------")
print ()
print ()

observationDict = {
    "spiller": 0,
    "tidspunkt": 0,
    "observation": "",
    "observant": ""
}

observationDict["observant"] = input('Observant: ')

while True:
    # message = input('Skriv noget til serveren: ')
    # clientSocket.sendto(message.encode(),(serverName, serverPort))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    observationDict["spiller"] = input('Spiller: ')
    observationDict["tidspunkt"] = current_time
    observationDict["observation"] = input('Observation: ')

    print(observationDict)

    message = str(observationDict)

    clientSocket.sendto(message.encode(),(serverName, serverPort))