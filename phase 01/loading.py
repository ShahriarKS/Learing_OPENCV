# ONE

import cv2


print(cv2.__version__)

#image reading

image=cv2.imread("imageFolder/vanG.jpg")

if image is None :
    print("error : image is not found")

else:
    print("image loaded successfully")