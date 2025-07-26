import numpy as np
import cv2 as cv
import os

# Specify the directory to save the video
save_dir = "C:\\Users\\STUDENT\\Pictures\\Group1\\Lab 2"
video_filename = os.path.join(save_dir, "Lab2.mp4")

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter(video_filename, fourcc, 30.0, (640, 480))  # Adjust frame size as needed

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if ret:
        # Display the resulting frame
        cv.imshow('frame', frame)

        # Write the frame to the video
        out.write(frame)

    else:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture and release the video writer
cap.release()
out.release()
cv.destroyAllWindows()
