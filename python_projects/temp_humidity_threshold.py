from dht11 import DHT11
import RPi.GPIO as GPIO
import LCD1602
from time import sleep
import MCP3008_simple as MCP3008

LCD1602.init(0x27, 1)
GPIO.setmode(GPIO.BOARD)

dht11_pin = 38
buzzer_pin = 40
pull_down_chgThreshold_pin = 36
GPIO.setup(pull_down_chgThreshold_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer_pin, GPIO.OUT, initial=GPIO.LOW)

mydht11 = DHT11(dht11_pin)

toggle_threshold = False
prev_toggle_state = 0
threshold = 0
try:
    while True:
        temp_humid = mydht11.read()
        read_button = GPIO.input(pull_down_chgThreshold_pin)
        pot_val = MCP3008.getResult(0, 10)
        threshold = round((100/1023)*pot_val)
        
        if read_button == 0 and prev_toggle_state == 1:
            toggle_threshold = not toggle_threshold
            print('haciendo el cambio')
            LCD1602.clear()
        
        if toggle_threshold == True:
            print('soy true')
            LCD1602.write(0, 0, 'Threshold: ')
            LCD1602.write(0, 1, 'Temp: ')
            LCD1602.write(8, 1, f"{threshold} ")
            LCD1602.write(11, 1, 'C')
            GPIO.output(buzzer_pin, 0)
            sleep(0.25)
            
        if toggle_threshold == False:
            if temp_humid.is_valid():
                temp = round(temp_humid.temperature)
                if temp >= threshold:
                    GPIO.output(buzzer_pin, 1)
                    LCD1602.write(0, 0, '!Alert!')
                    LCD1602.write(10, 1, f' {temp}')
                    LCD1602.write(0, 1, f"HIGH TEMP: ")
                    LCD1602.write(13, 1, ' C')
                    sleep(2)
                    GPIO.output(buzzer_pin, 0)
                    sleep(2)
                if temp <= threshold:
                    GPIO.output(buzzer_pin, 0)
                    LCD1602.write(0, 0, 'Temp: ')
                    LCD1602.write(7, 0, f"{temp} ")
                    LCD1602.write(10, 0, 'C')
                
        prev_toggle_state = read_button
        sleep(0.1)

except KeyboardInterrupt:
    LCD1602.clear()
    GPIO.cleanup()
    print('GPIO pins ready to go')




