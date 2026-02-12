import RPi.GPIO as GPIO
from time import sleep
import dht11

GPIO.setmode(GPIO.BOARD)

mydht = dht11.DHT11(pin = 40)

try:
    while True:
        result = mydht.read()
        if result.is_valid():
            msg = f"Temperatura: {result.temperature}. Humedad: {result.humidity}"
            print(f"Temperature is: {result.temperature}. Humidity is: {result.humidity}")
            print(len(msg.split()))
        sleep(0.2)

except KeyboardInterrupt:
    sleep(0.1)
    GPIO.cleanup()
    print('clean')