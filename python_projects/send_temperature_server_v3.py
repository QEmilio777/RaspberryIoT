from server_library import Server
import RPi.GPIO as GPIO
import dht11
from time import sleep


GPIO.setmode(GPIO.BOARD)
dht_pin = 40
sensor = dht11.DHT11(dht_pin)

sock = Server()
sock.begin("Server is up, and listening on port")

while True:
    
    cmd = sock.hear()
    
#     print("Received:", cmd, "from", sock.addr)
    
    if cmd == 'START':
        result = sensor.read()
        
        if result.is_valid():
            msg = f"TEMP={result.temperature};HUM={result.humidity}"
            sock.send(msg)
        
