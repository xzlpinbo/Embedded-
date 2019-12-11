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

# MQTT 메시지를 받았을 때, 콜백 함수
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    if msg.find(TURN_ON_COMMAND) != -1:
        wp.turn_on()
        sm.rotate(SERVO_ANGLE_OPEN)
    elif msg.find(TURN_OFF_COMMAND) != -1:
        wp.turn_off()
        sm.rotate(SERVO_ANGLE_CLOSE)

    # 메시지 로그
    print('')
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


if __name__ == '__main__':
    # 센서 초기화
    print('initializing')
    GPIO.setmode(GPIO.BCM)
    ifs = InfraredSensor(INFRARED_SENSOR_PIN)
    cmr = Camera(PHOTO_RESOLUTION)
    wp = WaterPump(WATER_PUMP_PIN1, WATER_PUMP_PIN2)
    sm = ServoMotor(SERVO_MOTOR_PIN)
    aws = AwsRekogntion()

    # MQTT 초기화
    print("creating new instance")
    client = mqtt.Client('raspberry_pi')  
    client.on_message = on_message 
    print("connecting to broker")
    client.connect(MQTT_BROKER_URL) 
    print("Subscribing to topic", MQTT_SUBSCRIBE)
    client.subscribe(MQTT_SUBSCRIBE)
    # 비동기식으로 메세지를 받는다.
    client.loop_start()

    ifs_cnt = 0

    try:
        while True:
            # 적외선 센서가 감지하면,
            if ifs.get_status() == INFRARED_SENSOR_DETECTED:
                print('ifs_cnt: ', ifs_cnt)
                ifs_cnt += 1
                time.sleep(1)
                # 정해진 시간이상 물체가 탐지하면,
                if ifs_cnt == OBJECT_DECTECTION_TIME:
                    ifs_cnt = 0
                    # 사진을 찍는다.
                    cmr.take_picture(PHOTO_DIR)
                    # 사진 속에 목표 물체가 있으면,
                    if aws.is_detect(PHOTO_DIR, TARGET_NAME):
                        print("CAT DETECTED")
                        # 워터 펌프와 서보 모터를 가동한다.
                        wp.turn_on()
                        sm.rotate(SERVO_ANGLE_OPEN)
                        time.sleep(3)
                        wp.turn_off()
                        sm.rotate(SERVO_ANGLE_CLOSE)
            else:
                ifs_cnt = 0
                time.sleep(1)
    # 프로그램을 종료시 할당된 자원을 반납한다.
    except KeyboardInterrupt:
        client.loop_stop()
        GPIO.output(WATER_PUMP_PIN, GPIO.LOW)
        GPIO.output(SERVO_MOTOR_PIN, GPIO.LOW)
        GPIO.cleanup()
