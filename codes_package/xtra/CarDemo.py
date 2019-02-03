import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
 
MotorThro_f = 35 #input
MotorThro_b = 37 #input

MotorDir_l = 31 #input
MotorDir_r = 33 #input


GPIO.setup(MotorThro_f,GPIO.OUT)
GPIO.setup(MotorThro_b,GPIO.OUT)
GPIO.setup(MotorDir_l,GPIO.OUT)
GPIO.setup(MotorDir_r,GPIO.OUT)

print ("forward motion")
GPIO.output(MotorThro_f,GPIO.HIGH)
GPIO.output(MotorThro_b,GPIO.LOW)

sleep(5)

print ("backward motion")
GPIO.output(MotorThro_f,GPIO.LOW)
GPIO.output(MotorThro_b,GPIO.HIGH)

sleep(5)

print ("stop")
GPIO.output(MotorThro_f,GPIO.LOW)
GPIO.output(MotorThro_b,GPIO.LOW)

sleep(5)

print ("left motion")
GPIO.output(MotorDir_l,GPIO.HIGH)
GPIO.output(MotorDir_r,GPIO.LOW)

sleep(5)

print ("right motion")
GPIO.output(MotorDir_l,GPIO.LOW)
GPIO.output(MotorDir_r,GPIO.HIGH)

sleep(5)

print ("stop")
GPIO.output(MotorDir_l,GPIO.LOW)
GPIO.output(MotorDir_r,GPIO.LOW)

sleep(3)


GPIO.cleanup()
