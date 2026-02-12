def main():
 import cv2
 image=cv2.imread("./images.png")
 if image is None:
    print("Error: Image not found at the specified location.")
 else:
    (h,w)=image.shape[:2]
    print(h,w)
    center=(w//2,h//2)

    M=cv2.getRotationMatrix2D(center,45,1.0)
    rotated_image=cv2.warpAffine(image,M,(600,700))
    cv2.imshow("Original Image",image)
    cv2.imshow("Rotated Image",rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__=="__main__":
     main()    