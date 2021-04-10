import socket
import datetime

print(datetime.datetime.now())

from localMachineInfo import print_machine_info

print_machine_info()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Insert host address: ")
print("Port scanning for: ", ip)

print("Insert start port and end port for scanning:")

start = input("Start port=> ")
end = input("End port => ")

startPort = int(start)
endPort = int(end)

def scanner(port):
    try:
        sock.connect((ip,port))
        return True
    except:
        return False

for portNumber in range(startPort,endPort):
    print("Scanning port ", portNumber)
    if scanner(portNumber):
        print('Port: ',portNumber,'/tcp',' is open!')