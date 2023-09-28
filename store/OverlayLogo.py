import cvzone
import cv2
#
# imgBack = cv2.imread("Resources/t1.jpg")
# imgFront = cv2.imread("Resources/l2.png", cv2.IMREAD_UNCHANGED)
# dim = (300, 300)
# imgFront = cv2.resize(imgFront,dim)
# imgFront = cv2.resize(imgFront, (0, 0), None, 0.3, 0.3)
#
# hf, wf, cf = imgFront.shape
# hb, wb, cb = imgBack.shape
#
# # imgResult = cvzone.overlayPNG(imgBack, imgFront, [0, hb-hf])
# imgResult = cvzone.overlayPNG(imgBack, imgFront, [150,100])
#
# cv2.imshow("Image", imgResult)
# cv2.waitKey(0)


# importing the module
import cv2
import os

def dress(logo=None,image=None):
    print(image)
    path = os.getcwd() +'/'+str(image)
    print(path)
    # function to display the coordinates of
    # of the points clicked on the image
    def click_event(event, x, y, flags, params):
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
            # displaying the coordinates
            # on the Shell
            print(x, ' ', y)

            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(img, str(x) + ',' +
            #             str(y), (x, y), font,
            #             1, (255, 0, 0), 2)

            imgFront = cv2.imread(os.getcwd()+'/store/Resources/l2.png', cv2.IMREAD_UNCHANGED)
            dim = (300, 300)
            imgFront = cv2.resize(imgFront,dim)
            imgFront = cv2.resize(imgFront, (0, 0), None, 0.3, 0.3)

            hf, wf, cf = imgFront.shape
            hb, wb, cb = img.shape

            # imgResult = cvzone.overlayPNG(imgBack, imgFront, [0, hb-hf])
            imgResult = cvzone.overlayPNG(img, imgFront, [x,y])

            cv2.imshow('image', imgResult)

        #checking for right mouse clicks
        # if event == cv2.EVENT_RBUTTONDOWN:
        #     # displaying the coordinates
        #     # on the Shell
        #     print(x, ' ', y)
        #
        #     # displaying the coordinates
        #     # on the image window
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     b = img[y, x, 0]
        #     g = img[y, x, 1]
        #     r = img[y, x, 2]
        #     cv2.putText(img, str(b) + ',' +
        #                 str(g) + ',' + str(r),
        #                 (x, y), font, 1,
        #                 (255, 255, 0), 2)
        #     cv2.imshow('image', img)


    # driver function

    # reading the image
    img = cv2.imread(path,1)
    print('a',img)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
    return
