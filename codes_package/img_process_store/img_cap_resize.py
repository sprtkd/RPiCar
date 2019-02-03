#this code captures a frame from the webcam
#and returns a resized matrix as needed

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def cap_img():
     _,frame = cap.read()
     img_mat = np.array(frame)
     return img_mat

def cam_exit():
    cap.release()
    cv2.destroyAllWindows()
