import numpy as np
import cv2 as cv

video_path = 'C:\\Users\\STUDENT\\Pictures\\Group1\\Lab 2\\Lab2.mp4'

cap = cv.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?), Exiting ...")
        break

    cv.imshow('frame', frame)
    if cv.waitKey(30) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
