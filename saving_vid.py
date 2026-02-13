def main():

 import cv2
 cap=cv2.VideoCapture(0)

 image_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 image_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
 codec=cv2.VideoWriter_fourcc(*'XVID')
 out=cv2.VideoWriter('output.avi',codec,20.0,(image_width,image_height))
 while True:
        ret,frame=cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow('frame',frame)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
 cap.release()
 cv2.destroyAllWindows()
if __name__ == "__main__":
    main()