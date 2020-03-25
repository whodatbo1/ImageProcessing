import cv2
import numpy as np


def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        text = ""
        text += str(img[y, x, 0]) + ", "
        text += str(img[y, x, 1]) + ", "
        text += str(img[y, x, 2])
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.imshow("Image", img)
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, "  ", y)
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow("Image", img)


img = cv2.imread("selfie.jpg", 1)
cv2.imshow("Image", img)

cv2.setMouseCallback("Image", clickEvent)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
