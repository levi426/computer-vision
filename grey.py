def main():

 import cv2
 location=input("enter location of the image: ")
 saved_image=input("enetr name of the saved image:" )

 image=cv2.imread(location)
 if image is None:
    print("Error: Image not found at the specified location.")
 else:
    grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey Image",grey_image)
    cv2.imwrite(saved_image,grey_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
if __name__=="__main__":
     main()    