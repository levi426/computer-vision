import cv2
import mediapipe as mp
import math
f_len=520
cam_dist=90
mpPose=mp.solutions.pose
pose_detector=mpPose.Pose()
draw_utils=mp.solutions.drawing_utils
camera=cv2.VideoCapture(0)

while True:
    ok,img=camera.read()
    if not ok:
        break
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    output=pose_detector.process(img_rgb)
    if output.pose_landmarks:
        height,width,_=img.shape
        lm=output.pose_landmarks.landmark


        nose_point=lm[mpPose.PoseLandmark.NOSE]
        nose_pixel_y=int(nose_point.y*height)


        l_ankle=lm[mpPose.PoseLandmark.LEFT_ANKLE]
        r_ankle=lm[mpPose.PoseLandmark.RIGHT_ANKLE]


        ankle_pixel_y=int(max(l_ankle.y,r_ankle.y)*height)
        pix_height=abs(ankle_pixel_y-nose_pixel_y)


        approx_height=(pix_height*cam_dist)/f_len

        cv2.putText(img,f"Height: {approx_height:.2f} inches ({approx_height*2.54:.2f} cm)",(30,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
        cv2.line(img,(int(nose_point.x*width),nose_pixel_y),(int(l_ankle.x*width),ankle_pixel_y),(0,0,255),2)


        draw_utils.draw_landmarks(img,output.pose_landmarks,mpPose.POSE_CONNECTIONS)
    cv2.imshow("height check",img)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
