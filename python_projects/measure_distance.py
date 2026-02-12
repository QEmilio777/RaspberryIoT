import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

echo_pin = 40
trig_pin = 38

GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(trig_pin, GPIO.OUT)

vel_sound = 343

try:
    while True:
        GPIO.output(trig_pin, 0)
        time.sleep(2E-6)
        GPIO.output(trig_pin, 1)
        time.sleep(10E-6)
        GPIO.output(trig_pin, 0)
        
        while GPIO.input(echo_pin) == 0:
            pass
        start = time.time()
        while GPIO.input(echo_pin) == 1:
            pass
        end = time.time()
        time_taken = end - start
        distance = vel_sound * (time_taken/2)
        
        print(f"Distance in cm: {round(distance*100, 2)}")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("--GPIO pins ready to go")

