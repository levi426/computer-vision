def main():
 import cv2
 
 image=cv2.imread("./images.png")
 if image is None:
    print("Error: Image not found at the specified location.")
 else:
    flipped_image=cv2.flip(image,0)
    cv2.imshow("Original Image",image)
    cv2.imshow("Flipped Image",flipped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
if __name__=="__main__":
        main()