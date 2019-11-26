import Ex_06_module as ex6
import sys 

if __name__ == "__main__":
    input_pin_num = sys.argv[1]
    input_led_mode = sys.argv[2]
    ex6.ledOnOff(input_pin_num, input_led_mode)


