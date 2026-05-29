#THREE


import cv2

print(cv2.__version__)

#image raeding

image=cv2.imread("imageFolder/vanG.jpg")

if image is not None :
    success = cv2.imwrite("imageFolder/output.jpg",image) # (je name save korte chao, je variable e rakhsila)

else :
    print("image is not saved")
