import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

rows = [11, 13, 15, 29]
columns = [31, 33, 35, 37]

keyPad = [[1, 2, 3, "A"], [4, 5, 6, "B"], [7, 8, 9, "C"], ["*", 0, "#", "D"]]

for i in rows:
    GPIO.setup(i, GPIO.OUT)

for i in columns:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    row = int(input("which row you want to read: "))
    column = int(input("which column you want to read: "))
    while True:
        GPIO.output(rows[row], True)
        butval = GPIO.input(columns[column])
        GPIO.output(rows[row], False)
        
        if butval:
            print(keyPad[row][column])
        
        # print(butval)
        sleep(0.2)
            

except KeyboardInterrupt:
    sleep(0.1)
    GPIO.cleanup()
    print("gpio good to go")










