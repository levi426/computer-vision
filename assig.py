import cv2
import cv2
REAL_HEIGHT = 7.5      
KNOWN_DISTANCE = 90
points = []
def mouse_callback(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

cap = cv2.VideoCapture(0)
cv2.namedWindow("focal length")
cv2.setMouseCallback("focal length", mouse_callback)

print("1. place object at the specified distance.")
print("2. click up and lower of te object")


while True:
    ret,frame=cap.read()
    if not ret:
        break
    for point in points:
        cv2.circle(frame, point, 5,(0, 0, 255),-1)
    cv2.imshow("focal length", frame)
    if len(points) == 2:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

if len(points) == 2:
    pixel_height = abs(points[0][1] - points[1][1])
    focal_length = (pixel_height * KNOWN_DISTANCE) / REAL_HEIGHT
    
    print(f"pixel height: {pixel_height} pixels")
    print(f"estimated focal length: {focal_length:.2f} pixels")
else:
    print("Calibration cancelled.")
