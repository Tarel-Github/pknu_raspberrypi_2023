# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17; green = 27; blue = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, False)
GPIO.output(green, False)
GPIO.output(blue, False)


try:
    while True:
        GPIO.output(red, True)
        time.sleep(0.5)

        GPIO.output(red, False)


except KeyboardInterrupt:
    GPIO.cleanup()
