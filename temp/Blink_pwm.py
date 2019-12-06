import time

import RPi.GPIO as GPIO

LedPin = 18

pwmPin = 18
pwm = ''
dc = 60  # duty cycle(0-100)


def setup():
    global pwm
    global dc
    GPIO.setmode(GPIO.BCM)  # use BCM Pin number
    GPIO.setup(pwmPin, GPIO.OUT)
    pwm = GPIO.PWM(pwmPin, dc)
    print("pwmPin = %d" % pwmPin)
    print("Mode = OUT, duty cycle : %d" % dc)


def blink():
    global pwm
    global dc
    dt = 10
    pwm.start(dc)
    while True:
        if (dc == 100) or (dc == 10):
            dt *= -1
            dc += dt
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)


def destroy():
    global pwm
    pwm.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()
