import socket
from time import sleep
bufferSize = 1024
msgFromServer="Hello client, I am the server"
ServerPort = 2222
ServerIP = "192.168.1.63"
bytesToSend = msgFromServer.encode('utf-8')
RPISocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPISocket.bind((ServerIP, ServerPort))
print('Server is up and listening...')
counter = 0
while True:
    message, address = RPISocket.recvfrom(bufferSize)
    message = message.decode('utf-8')
    print(message)
    print('client Address', address[0])
    if message == 'increment':
        counter += 1
    if message == 'decrement':
        counter -= 1
    msg = str(counter)
    msg = msg.encode('utf-8')
    RPISocket.sendto(msg, address)
