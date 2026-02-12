from server_library import Server
import RPi.GPIO as GPIO
import dht11

GPIO.setmode(GPIO.BOARD)
dht_pin = 40
dht = dht11.DHT11(dht_pin)

server = Server()
server.begin("Ready to send some data from: ")

def msg(request, result):
    return f"The {request.capitalize()} is: {result}"

while True:
    request = server.hear()
    result = dht.read()
    if result.is_valid():
        if request.lower() == "temperature":
            result = result.temperature
            server.send(msg(request, result))
            
        if request.lower() == "humidity":
            result = result.humidity
            server.send(msg(request, result))
        
        else:
            server.send('')
    else:
        server.send('')
            
            
            