import cv2

img = cv2.imread('C:/Users/MORI/Documents/Coding/Python/OpenCV/images/Audi A4.jpg')

# Resizing an image.
# original image size: 750x484p

imgSize = cv2.resize(img, (750, 484))    # (height, width), units: pixels.
print(img.shape)    # print size of the image

cv2.imshow('Resized Image', imgSize)

# Cropping an image
imgCrop = img[0: 200, 200:700]     # (height, width)

cv2.imshow('Cropped Image', imgCrop)

cv2.waitKey(0)
