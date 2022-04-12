import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # (512, 512) is the size of the matrix.
print(img.shape)

# Color image
# img[:] = 69, 69, 241    # Image is blue in color.

# Creating lines
# cv2.line(img, (0, 0), (300, 300), (13, 177, 13), 5)   # starting point: (0, 0); ending point: (300, 300); color: (13, 177, 13); line thickness: 5.

# alternatively used img.shape to specify starting point and ending point.
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (13, 177, 13), 5)

# Drawing a rectangle
cv2.rectangle(img, (20, 20), (250, 280), (69, 241, 69), 3)
# Fill rectangle.
cv2.rectangle(img, (20, 20), (250, 280), (69, 241, 69), cv2.FILLED)

# Drawing a circle.
cv2.circle(img, (450, 450), 30, (255, 255, 0), 5)   # center: (450, 450); radius: 30; color: (255, 255, 0); thickness: 5.

# Put text on images
cv2.putText(img, 'Learning opencv', (100, 100), cv2.FONT_HERSHEY_TRIPLEX, 6, (13, 177, 13, 1))   # (img, text, origin, font, scale, color,
# thickness) increasing value of the scale increases thickness of the text.


cv2.imshow('Image', img)

cv2.waitKey(0)
