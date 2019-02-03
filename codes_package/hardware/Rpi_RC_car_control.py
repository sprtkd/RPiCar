import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#init
motor_throttle_l = 31 # input pin
motor_throttle_r = 33 # input pin
motor_dir_l = 35 # input pin
motor_dir_r = 37 # input pin

GPIO.setup(motor_throttle_l,GPIO.OUT)
GPIO.setup(motor_throttle_r,GPIO.OUT)
GPIO.setup(motor_dir_l,GPIO.OUT)
GPIO.setup(motor_dir_r,GPIO.OUT)


def move_fwd_start():
        GPIO.output(motor_throttle_l,GPIO.HIGH)
        GPIO.output(motor_throttle_r,GPIO.LOW)

        
def throttle_stop():
        GPIO.output(motor_throttle_l,GPIO.LOW)
        GPIO.output(motor_throttle_r,GPIO.LOW)

        
def move_bckwd_start():
        GPIO.output(motor_throttle_l,GPIO.LOW)
        GPIO.output(motor_throttle_r,GPIO.HIGH)

        
def turn_left_start():
        GPIO.output(motor_dir_l,GPIO.HIGH)
        GPIO.output(motor_dir_r,GPIO.LOW)

        
def turn_right_start():
        GPIO.output(motor_dir_l,GPIO.LOW)
        GPIO.output(motor_dir_r,GPIO.HIGH)

        
def dir_stop():
        GPIO.output(motor_dir_l,GPIO.LOW)
        GPIO.output(motor_dir_r,GPIO.LOW)
        
def car_exit():
    GPIO.cleanup()
    
