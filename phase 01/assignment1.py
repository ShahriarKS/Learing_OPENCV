
# phase 1

import cv2

path = input("enter the path :")

imgUser = cv2.imread(path)

pref = input("press 1 for image showing or press two for image saving : ")

if pref == "1" :
    title =input("enter the title of the image window : ")
    cv2.imshow(title,imgUser)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif pref == "2":
    outName =input( "enter the name of the image you wanna make a save : ")
    Simg = cv2.imwrite(outName,imgUser)
    if Simg :
        print("saved successfully")

    else :
        print("didn't save yet") 
