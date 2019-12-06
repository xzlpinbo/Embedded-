import time

import RPi.GPIO as GPIO

pwmPin = 18
readPin = 20
pwm = ''
dt = 10
dc = 60 #duty cycle(0-100)

def setup():
    global pwm
    global dc
    GPIO.setMode(GPIO.BCM) # use BCM Pin number
    GPIO.setup(pwmPin, GPIO.OUT)
    GPIO.setup(readPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(readPin, GPIO.RISING, callback = handler)
    pwm = GPIO.PWM(pwm, dc)
    pwm.start(dc)
    print("pwmPin = %d" % pwmPin)
    print("Mode = OUT, duty cycle : %d" % dc)
    print("readPin = %d" % readPin)
    print("Mode = IN, PULL_UP")

def handler(channel):
    global dc
    global dt
    global pwm

    if (dc ==100) or (dc==0):
        dt*= -1
    dc += dt
    pwm.ChaneDutyCycle(dc)

def destroy():
    global pwm
    pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()