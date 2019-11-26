import Ex_06_module as ex6
import sys 


def setup():
    input_led_mode = input('set pin number > ')
    print("LedPin = %d" % pinNum)

if __name__ == "__main__":
    input_led_mode = sys.argv[1]
    ex6.ledOnOff(input_led_mode)


