import socket
import dht11
import RPi.GPIO as GPIO
from time import sleep

# ---------- DHT11 ----------
GPIO.setmode(GPIO.BOARD)
DHT_PIN = 40
sensor = dht11.DHT11(DHT_PIN)

# ---------- UDP ----------
SERVER_IP = "0.0.0.0"   # escucha en todas las interfaces
SERVER_PORT = 2222
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("UDP server listening on port", SERVER_PORT)

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    cmd = data.decode().strip()

    print("Received:", cmd, "from", addr)

    if cmd == "START":
        result = sensor.read()

        if result.is_valid():
            msg = f"TEMP={result.temperature};HUM={result.humidity}"
            sock.sendto(msg.encode(), addr)
#         else:
#             msg = "ERROR=DHT"
# 
#     else:
#         msg = "ERROR=CMD"