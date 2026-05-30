
#rotate an image
import cv2
img = cv2.imread("imageFolder/vanG.jpg")
 
if img is None :
    print("the img is not loaded")  
else :
    print("image loaded")

    (h,w) = img.shape[:2]
    center = (w//2, h//2)

    # thats how you rotate an image by 90 degrees
    
    M= cv2.getRotationMatrix2D(center,  90,1.0)
    rotatedImg =cv2.warpAffine(img, M, (w,h))

    print("Original image shape:", img.shape)

    cv2.imshow("original one",img)
    cv2.imshow("rotated one",rotatedImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()