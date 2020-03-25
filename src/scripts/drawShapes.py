import cv2 as cv2
import numpy as np

img = cv2.imread("selfie.jpg", 1)

#img =  np.zeros([1000, 1000, 3], np.uint8)

height, width, channels = img.shape
print (height, width, channels)
img = cv2.line(img, (0, 0), (width, height), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (0, height), (width, 100), (255, 0, 0), 1)

img = cv2.rectangle(img, (100, 100), (200, 200), (255, 255, 255), -1)
img = cv2.circle(img, (int(width/2), int(height/2)), 30, (0, 0, 0), -1)

font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.putText(img, "HAHAHA", (100, 100), font, 3.2 , (255, 255, 255), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()