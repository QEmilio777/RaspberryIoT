import RPi.GPIO as GPIO
import time

LED_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

try:
    
    while True:
        
        for duty in range(0, 101, 1):
            pwm.ChangeDutyCycle(duty)
            print(f"Brillo: {duty}%")
            time.sleep(1)
        
        for duty in range(100, -1, -1):
            pwm.ChangeDutyCycle(duty)
            print(f"Brillo: {duty}%")
            time.sleep(1)
    
    
except KeyboardInterrupt:
    time.sleep(0.1)
    print("Programa detenido de manera correcta")
finally:
    time.sleep(0.1)
    pwm.stop()
    del pwm
    GPIO.cleanup()
    print("Pines libre")