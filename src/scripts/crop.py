import cv2
import numpy as np

image = cv2.imread("selfie.jpg")
#print(image);
crop = image[10:10, 20:10]
#cv2.imshow("n", image)
print(crop)
#cv2.waitKey(0) & 0xFF == ord('q')

import cv2
y = 10
x = 10
w = 100
h = 50
img = cv2.imread("selfie.jpg")
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)