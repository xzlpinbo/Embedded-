import time

import RPi.GPIO as GPIO
from threading import Thread
import picamera
import boto3


# class InfraredSensor(Thread):
#     def __init__(self, irpin):
#         super().__init__()
#         self.irpin = irpin
#         self.is_running = False
#         self.status = 0
#         GPIO.setup(self.irpin, GPIO.IN)
#
#     def turn_on(self):
#         self.is_running = True
#
#     def turn_off(self):
#         self.is_running = False
#
#     def get_status(self):
#         return self.status
#
#     def run(self):
#         while self.is_running:
#             self.status = GPIO.input(self.irpin)
#             time.sleep(0.1)

class InfraredSensor():
    def __init__(self, irpin):
        super().__init__()
        self.irpin = int(irpin)
        self.is_running = False
        GPIO.setup(self.irpin, GPIO.IN)

    def get_status(self):
        return GPIO.input(self.irpin)


class WaterPump:
    def __init__(self, in1, in2):
        self.in1 = int(in1)
        self.in2 = int(in2)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def turn_off(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)


class ServoMotor:
    def __init__(self, servo_pin):
        self.servo_pin = int(servo_pin)
        self.pwm = GPIO.PWM(self.servo_pin, 100)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        # GPIO.setmode(GPIO.BCM)
        
        self.pwm.start(2.5)  # Initialisierung

    def __del__(self):
        self.pwm.stop()

    def rotate(self, angle):
        dc = ((float(angle) / 180.0) + 1.0) * 5.0
        self.pwm.ChangeDutyCycle(dc)


class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_picture(self, _dir):
        camera = picamera.PiCamera()
        camera.resolution = self.resolution
        camera.capture(_dir)
        time.sleep(1)
        camera.close()

class AwsRekogntion:
    def __init__(self):
        self.client = boto3.client('rekognition')

    def is_detect(self, photo_dir, target_name):
        print('send picture to aws')

        with open(photo_dir, 'rb') as image:
            response = self.client.detect_labels(Image={'Bytes': image.read()})

        print('Detected labels in ' + photo_dir)
        for label in response['Labels']:
            print(label['Name'] + ' : ' + str(label['Confidence']))
            if label == target_name:
                return True
        return False

