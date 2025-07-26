import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

# Define the code and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'MJPG’)
out = cv.VideoWriter(‘Lab2.mp4’, fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
    print("Can't receive frame (stream end?). Exiting …")
    break

    cv.imshow(‘frame’, frame)
    if cv.waitKey(1) == ord(‘q’):
    break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
