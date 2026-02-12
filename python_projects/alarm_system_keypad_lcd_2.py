import RPi.GPIO as GPIO
from time import sleep
import LCD1602 as lcd
from keypad_memory import Keypad

motion_sensor_pin = 32
buzzer_pin = 38

keypad = Keypad()
keypad.begin()
lcd.init(0x27, 1)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(motion_sensor_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT, initial=GPIO.LOW)

mode = ""
switch = False
sensor = False
password = ["1", "9", "7", "D"]

sleep(15)


try:
    while True:
        lcd.clear()
        lcd.write(0, 0, "'C' to engage")
        lcd.write(0, 1, "'B' chng password")
        mode = keypad.return_values()
        lcd.clear()
#         if engage == "C":
#             switch = True
#         else:
#             lcd.clear()
#             lcd.write(0, 0, "Wrong key")
#             sleep(2)
        match mode:
            case "C":
                switch = True
                while switch:
                    read_sensor = GPIO.input(motion_sensor_pin)
                    print(read_sensor)
                    if read_sensor:
                        sensor = True
                    if sensor:
                        lcd.clear()
                        lcd.write(0, 0, "Input password: ")
                        GPIO.output(buzzer_pin, 1)
                        entered_password = keypad.return_values()
                        if list(entered_password) == password:
                            lcd.clear()
                            lcd.write(0, 0, "Correcto!")
                            GPIO.output(buzzer_pin, 0)
                            switch = False
                            sensor = False
                            sleep(2)
                            lcd.clear()
                        else:
                            lcd.clear()
                            lcd.write(0, 0, "Wrong password")
                            sleep(2)
                    if not sensor:
                        lcd.write(0, 0, "ACTIVADO")
            
            case "B":
                lcd.write(0, 0, "Old password")
                old_password = list(keypad.return_values())
                if old_password == password:
                    lcd.write(0, 0, "New password")
                    password = list(keypad.return_values())
                    lcd.clear()
                    lcd.write(0, 0, "Password changed")
                    sleep(2)
                if old_password != password:
                    lcd.clear()
                    lcd.write(0, 0, "Wrong password")
                    sleep(2)
            
        
except KeyboardInterrupt:
    sleep(0.1)
    GPIO.cleanup()
    lcd.clear()
    print("GPIO pins ready to go")
    
    
    
