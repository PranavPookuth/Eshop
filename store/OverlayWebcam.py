import cvzone
import cv2


cap = cv2.VideoCapture(0)
success, img = cap.read()

imgFront = cv2.imread("Resources/logo.png", cv2.IMREAD_UNCHANGED)
imgFront = cv2.resize(imgFront, (0, 0), None, 0.3, 0.3)

hf, wf, cf = imgFront.shape
hb, wb, cb = img.shape

fpsReader = cvzone.FPS()

while True:
    success, img = cap.read()
    imgResult = cvzone.overlayPNG(img, imgFront, [0, hb-hf])
    _, imgResult = fpsReader.update(imgResult)
    cv2.imshow("Image", imgResult)
    cv2.waitKey(1)



