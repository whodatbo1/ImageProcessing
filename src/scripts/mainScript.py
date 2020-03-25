import numpy as np
import cv2
print("Hello")
img = cv2.imread("selfie.jpg", 1)
print(img)
cv2.imshow("Window", img)
cv2.waitKey(0) & 0xFF
cv2.imwrite("greySelfie.jpg", img)