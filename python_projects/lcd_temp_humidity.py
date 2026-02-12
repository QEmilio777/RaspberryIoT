import RPi.GPIO as GPIO
from dht11 import DHT11
import LCD1602
from time import sleep

LCD1602.init(0x27, 1)

GPIO.setmode(GPIO.BOARD)

dht11_pin = 40
mydht11 = DHT11(pin = dht11_pin)

pull_down_resistor_pin = 38
GPIO.setup(pull_down_resistor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_state = 0
toggle = False
temp = float
humid = float

try:
    while True:
        read_temp_humid = mydht11.read()
        read_pull_down = GPIO.input(pull_down_resistor_pin)
        if read_temp_humid.is_valid():
            temp = read_temp_humid.temperature
            humid = read_temp_humid.humidity
            
            if read_pull_down == 0 and prev_state == 1:
                toggle = not toggle
                LCD1602.clear()
                if toggle:
                    LCD1602.write(0, 0, f"Changing To")
                    LCD1602.write(0, 1, f"Fahrenheit")
                    sleep(2)
                    LCD1602.clear()
                else:
                    LCD1602.write(0, 0, f"Changing To")
                    LCD1602.write(0, 1, f"Celsius")
                    sleep(2)
                    LCD1602.clear()
                print('limpio')
            
            
            if toggle:
                temp = round((temp + 32) * 9/5, 2)
            
                
            LCD1602.write(0, 0, f"Temp: {temp}")
            LCD1602.write(0, 1, f"Humid: {humid}")
            
            prev_state = read_pull_down
            
            sleep(0.2)

except KeyboardInterrupt:
    sleep(0.2)
    LCD1602.clear()
    GPIO.cleanup()
    print('--everything ready to go')

