import time

import RPi.GPIO as GPIO

LedPin = 21


def setup():
    GPIO.setmode(GPIO.BCM)  # use BCM Pin number
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)
    print("LedPin = %d" % LedPin)
    print("Mode = OUT, PULL_UP")


def blink():
    while True:
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(1)

def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()