import time

import RPi.GPIO as GPIO

LedPin = 21
ReadPin = 20


def setup():
    GPIO.setmode(GPIO.BCM)  # use BCM Pin number
    GPIO.setup(ReadPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)
    print("LedPin = %d" % LedPin)
    print("Mode = OUT")
    print("ReadPin = %d" % ReadPin)
    print("Mode = IN, PULL_UP")


def blink():
    while True:
        btn = GPIO.input(ReadPin)
        print(btn)
        if btn == False:
            GPIO.output(LedPin, GPIO.HIGH)
        else:
            GPIO.output(LedPin, GPIO.LOW)
        time.sleep(0.1)


def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()
