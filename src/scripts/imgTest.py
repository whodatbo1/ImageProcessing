import cv2
import numpy as np

img = cv2.imread("selfie.jpg", 1)

width, height, channels = img.shape
print(width * height * channels)
print("Shape: ", img.shape)
print("Size: ", img.size)
print("Type ", img.dtype)

b, g, r = cv2.split(img)
print(b[0])
print(img[0][0])
img = cv2.merge((b, g, r))
print("Shape: ", b.shape)
print("Size: ", b.size)
print("Type ", b.dtype)

img = np.zeros((512, 512), 'uint8')
print(img)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
