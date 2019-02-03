import picamera
print("About to take a picture...")
with picamera.PiCamera() as camera:
    camera.resolution= (1024,768)
    camera.capture("/home/pi/Desktop/SelfDrivingCar/codes_package/hardware/image.jpg")
