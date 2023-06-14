# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17
green = 27
blue = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    while True:
        GPIO.output(red, False)     # RED on
        GPIO.output(green, True)
        GPIO.output(blue, True)
        time.sleep(0.5)

        GPIO.output(red, True)
        GPIO.output(green, False)
        GPIO.output(blue, True)
        time.sleep(0.5)

        GPIO.output(red, True)
        GPIO.output(green, True)
        GPIO.output(blue, False)
        time.sleep(0.5)



except KeyboardInterrupt:
    GPIO.cleanup()
