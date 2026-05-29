#FOUR

#dimension

#(height,width,channel)// channel =3 means RGB , channels = 2 means gray scale

import cv2

img = cv2.imread('imageFolder/vanG.jpg')

if img is not None :
   h,w,c = img.shape
   print(f"image loaded .\n height : {h} \n width : {w} \n channels : {c}")
else :
   print("no dimesion")   