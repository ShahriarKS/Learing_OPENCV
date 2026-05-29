#TWO

# three functions 

# imshow("title",variable) -> it creates a window to show the image
# waitkey(0) ->wait untill user presses any key ,then close the window. 0 means infinte wait
#destroyAllwindows

import cv2

image=cv2.imread("imageFolder/vanG.jpg")

if image is not None : 
 cv2.imshow("van gogh er chobi",image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()

else :
 print("not showing") 