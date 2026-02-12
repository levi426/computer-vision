def mian():
 import cv2
 
 image=cv2.imread("./images.png")
 if image is None:
    print("Error: Image not found at the specified location.")
 else:
    sliced_image=image[100:400,50:300]
    cv2.imshow("Original Image",image)
    cv2.imshow("Sliced Image",sliced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
if __name__=="__main__":
        mian()