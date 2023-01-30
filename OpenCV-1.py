import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(2) & 0xff == 27:
        break
cam.release()
cv2.destroyAllWindows()