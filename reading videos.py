import cv2
import numpy as np
video = cv2.VideoCapture('C:/Users/MORI/Documents/Coding/Python/OpenCV/videos/demo.mp4')

while True:
    success, img = video.read()
    cv2.imshow('Demo video', img)

    # add a key press to terminate the program.
    if cv2.waitKey(20) & 0xFF == ord('q'):      # increasing waitKey value plays the video in slow motion.
        break
