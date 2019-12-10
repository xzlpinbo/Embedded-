from SensorTools import *
import time

import RPi.GPIO as GPIO

import paho.mqtt.client as mqtt

# 센서 핀 설정
INFRARED_SENSOR_PIN = 20
WATER_PUMP_PIN1 = 23
WATER_PUMP_PIN2 = 24
SERVO_MOTOR_PIN = 21

# 적외선 센서 탐지시 결과 값
INFRARED_SENSOR_DETECTED = 0

# 연속적으로 적외선이 감지하는 시간
OBJECT_DECTECTION_TIME = 5

# 사진 설정
PHOTO_RESOLUTION = (256, 256)
PHOTO_DIR = './photo.jpg'

# 감지할 대상 이름
TARGET_NAME = 'Cat'

# 서보 모터가 움직일 각도
SERVO_ANGLE_OPEN = 180
SERVO_ANGLE_CLOSE = 400

# MQTT 로 부터 반응할 명령어들
TURN_ON_COMMAND = 'ON'
TURN_OFF_COMMAND = 'OFF'

# MQTT 설정들
MQTT_BROKER_URL = 'test.mosquitto.org'
MQTT_SUBSCRIBE = 'konkuk/emb/test'



# def on_message(client, userdata, message):
#     print('')
#     print("message received ", str(message.payload.decode("utf-8")))
#     print("message topic=", message.topic)
#     print("message qos=", message.qos)
#     print("message retain flag=", message.retain)

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    if msg.find(TURN_ON_COMMAND) != -1:
        wp.turn_on()
        sm.rotate(SERVO_ANGLE_OPEN)
    elif msg.find(TURN_OFF_COMMAND) != -1:
        wp.turn_off()
        sm.rotate(SERVO_ANGLE_CLOSE)

    print('')
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


if __name__ == '__main__':
    print('initializing')
    GPIO.setmode(GPIO.BCM)
    ifs = InfraredSensor(INFRARED_SENSOR_PIN)
    cmr = Camera(PHOTO_RESOLUTION)
    wp = WaterPump(WATER_PUMP_PIN1, WATER_PUMP_PIN2)
    sm = ServoMotor(SERVO_MOTOR_PIN)
    aws = AwsRekogntion()

    print("creating new instance")
    client = mqtt.Client('raspberry_pi')  # create new instance
    client.on_message = on_message  # attach function to callback
    print("connecting to broker")
    client.connect(MQTT_BROKER_URL)  # connect to broker
    print("Subscribing to topic", MQTT_SUBSCRIBE)
    client.subscribe(MQTT_SUBSCRIBE)
    client.loop_start()

    ifs_cnt = 0

    try:
        while True:
            if ifs.get_status() == INFRARED_SENSOR_DETECTED:
                print('ifs_cnt: ', ifs_cnt)
                ifs_cnt += 1
                time.sleep(1)
                if ifs_cnt == OBJECT_DECTECTION_TIME:
                    ifs_cnt = 0
                    cmr.take_picture(PHOTO_DIR)
                    if aws.is_detect(PHOTO_DIR, TARGET_NAME):
                        print("CAT DETECTED")
                        wp.turn_on()
                        sm.rotate(SERVO_ANGLE_OPEN)
                        time.sleep(3)
                        wp.turn_off()
                        sm.rotate(SERVO_ANGLE_CLOSE)
            else:
                ifs_cnt = 0
                time.sleep(1)

    except KeyboardInterrupt:
        client.loop_stop()
        GPIO.output(WATER_PUMP_PIN, GPIO.LOW)
        GPIO.output(SERVO_MOTOR_PIN, GPIO.LOW)
        GPIO.cleanup()
