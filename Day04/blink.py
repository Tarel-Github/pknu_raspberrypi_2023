import RPi._GPIO as GPIO
import time

signal_pin = 18

# GPIO.setmode(GPIO.BOARD)    # 1 ~ 40
GPIO.setmode(GPIO.BCM)        # GPIO 18, GROUND
GPIO.setup(signal_pin, GPIO.OUT) # GPIO18핀에다가 출력을 설정

while (True):
    GPIO.output(signal_pin, True)   # GPIO18핀에 전압시그널 온
    time.sleep(0.1)       # 2초동안 불킴
    GPIO.output(signal_pin, False)  # GPIO18핀에 전압시그널 오프
    time.sleep(0.1)       # 1초동안 불끔