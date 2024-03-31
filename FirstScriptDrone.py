from djitellopy import Tello
import KeyPressModule as kp
from time import sleep
import cv2
#import ImageCapture

from DJITelloPy.djitellopy import tello

kp.init()
tello = Tello()

tello.connect()
print(tello.get_battery())
tello.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed
    
    if kp.getKey("DOWN"): fb = -speed
    elif kp.getKey("UP"): fb = speed
    
    if kp.getKey("s"): ud = -speed
    elif kp.getKey("w"): ud = speed    
    
    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed
    
    if kp.getKey("q"): tello.land()
    if kp.getKey("e"): tello.takeoff()
    
    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    #sleep(0.05)