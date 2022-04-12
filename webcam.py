import cv2

webcam = cv2.VideoCapture(0)
webcam.set(3, 640)  # (id, width)
webcam.set(4, 480)  # (id, height)

# Adjust brightness
webcam.set(10, 2000)    # (id, brightness)

while True:
    success, img = webcam.read()
    cv2.imshow('Webcam', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
