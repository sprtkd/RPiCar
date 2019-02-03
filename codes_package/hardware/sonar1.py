import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23 #pins
GPIO_ECHO = 24 #pins

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.output(GPIO_TRIGGER, 0)
GPIO.setup(GPIO_ECHO, GPIO.IN)


GPIO.output(GPIO_TRIGGER, 1)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, 0)

#Start_time = time.time()
#Stop_time = time.time()

while GPIO.input(GPIO_ECHO) == 0:
    pass
Start_time = time.time()

while GPIO.input(GPIO_ECHO) == 1:
    pass
Stop_time = time.time()

distance = (Stop_time - Start_time) * 17000
print(float(distance))

GPIO.cleanup()

