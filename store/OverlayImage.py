import cvzone
import cv2
import numpy as np

# imgBack = cv2.imread("Resources/nature.jpg")
imgBack = np.ones((480, 640, 3), np.uint8)
imgFront = cv2.imread("Resources/gear.png", cv2.IMREAD_UNCHANGED)
imgFront = cv2.resize(imgFront, (0, 0), None, 0.5, 0.5)

imgResult = cvzone.overlayPNG(imgBack, imgFront, [100, 100])

cv2.imshow("Image", imgResult)
cv2.waitKey(0)
