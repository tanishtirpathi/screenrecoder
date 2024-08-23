import cv2
import pyautogui
import time
import numpy as np
from win32api import GetSystemMetrics
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimensions  = (width, height)
vio = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4", vio,30.0,dimensions)
now_tim= time.time()
dur = 20
end_time = now_tim + dur
while True:
    print(" recoding")
    image = pyautogui.screenshot()
    frame_i =np.array(image)
    frame = cv2.cvtColor(frame_i, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time= time.time()
    if c_time > end_time:
        break
output.release()
print("complete recoding")    
    
    