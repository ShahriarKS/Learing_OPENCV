
#FIVE

#cv2.cvtColor(kon picture_convert_করবা, কোন type_conversion)

import cv2

img = cv2.imread("imageFolder/vanG.jpg")

grayC=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("convert kora chobi",grayC)
cv2.waitKey(0)
cv2.destroyAllWindows()

Cdone=cv2.imwrite("imageFolder/Cimg.jpg",grayC)