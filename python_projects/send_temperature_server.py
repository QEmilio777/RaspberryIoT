import socket
from time import sleep
import dht11
import RPi.GPIO as GPIO

dht_pin = 40
mydht = dht11.DHT11(dht_pin)

GPIO.setmode(GPIO.BOARD)

bufferSize = 1024
msgFromServer="Hello client, I am the server"
ServerPort = 2222
ServerIP = "192.168.1.63"
bytesToSend = msgFromServer.encode('utf-8')
RPISocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPISocket.bind((ServerIP, ServerPort))
print('Server is up and listening...')

try:
    while True:
        message, address = RPISocket.recvfrom(bufferSize)
        message = message.decode('utf-8')
        print(message)
        if message == "Start":
            result = mydht.read()   
            if result.is_valid():
                msg = f"Temperatura: {result.temperature}. Humedad: {result.humidity}"
                msg = msg.encode('utf-8')
                RPISocket.sendto(msg, address)
                print('Client Address: ', address[0])
            if result.is_valid() == False:
                msg = "no"
                msg = msg.encode('utf-8')
                RPISocket.sendto(msg, address)
                print('Client Address: ', address[0])
        if message != "Start":
            msg = f"Invalid request"
            msg = msg.encode('utf-8')
            RPISocket.sendto(msg, address)
        sleep(2)
    #     if message == 'increment':
    #         counter += 1
    #     if message == 'decrement':
    #         counter -= 1
    #     msg = str(counter)
    #     msg = msg.encode('utf-8')
    #     RPISocket.sendto(msg, address)


except KeyboardInterrupt:
    GPIO.cleanup()
    print("pins ready to go")
    

