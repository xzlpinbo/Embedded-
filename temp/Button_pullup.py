import time

import RPi.GPIO as GPIO

toggle = True


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(18, GPIO.RISING, callback=handler)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)


def handler(channel):
    global toggle
    toggle = not toggle
    GPIO.output(23, toggle)
    GPIO.output(24, not toggle)


def destory():
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        destory()
