
#cropping
#image[startY:endY, startX:endX] y height and x width er jonno

import cv2
img=cv2.imread("imageFolder/vanG.jpg")

if img is None :
    print("the img is not loaded")
else :
    print("image loaded")
    croppedImg = img[400:600, 100:500]

    print("Original image shape:", img.shape)

    cv2.imshow("original one",img)
    cv2.imshow("cropped one",croppedImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()