def mian():
 import cv2

 image=cv2.imread("./images.png")
 if image is None:
    print("Error: Image not found at the specified location.")
 else:
    resized_image=cv2.resize(image,(400,400))
    cv2.imshow("Resized Image",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
if __name__=="__main__":
     mian()
