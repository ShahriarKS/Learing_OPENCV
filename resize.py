
#One

# variable = library .resize( src ,dsize , fx, fy , interpolation)
# src = kon chobi k resize korba
# dszie = je dimension e resize korte chai 
# (width, height)

import cv2
img=cv2.imread("imageFolder/vanG.jpg")

if img is None :
    print("the img is not resized")

else :
    print("image loaded")
    resizedImg = cv2.resize(img,(500,500))

    print("Original image shape:", img.shape)

    cv2.imshow("original one",img)
    cv2.imshow("resized one",resizedImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


