import RPi.GPIO as GPIO
import time

pwm_pin = 18
GPIO.setwarnings(False)  # 오류메시지 제거
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 50)
pwm.start(3.0)  # 3 or 3.0

for i in range(0, 3):
    for high in range(30, 125):
        pwm.ChangeDutyCycle(high/10.0)
        print(f'각도 : {(30)}')
        time.sleep(0.02)

    for low in range(124, 30, -1):
        pwm.ChangeDutyCycle(low/10.0)
        time.sleep(0.02)

pwm.ChangeDutyCycle(0)
pwm.stop()
GPIO.cleanup()