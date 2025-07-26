# Sobel - x, y, xy, og
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('Original', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
    filtered_image_x = cv.convertScaleAbs(sobelx)
    sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
    filtered_image_y = cv.convertScaleAbs(sobely)
    sobelxy = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelxy)

    cv.imshow('Sobel X', filtered_image_x)
    cv.imshow('Sobel Y', filtered_image_y)
    cv.imshow('Sobel XY', filtered_image_xy)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()



# Canny - canny, og
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(image=gray,threshold1=100,threshold2=200)

    cv.imshow('Original', frame)
    cv.imshow('Canny', edges)

    # Check for the 'q' key to quit
    if cv.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture and the VideoWriter
cap.release()
cv.destroyAllWindows()



# Laplacian - og, laplacian
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('Original', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    laplacian = cv.Laplacian(src=gray, ddepth=cv.CV_64F)
    filtered_image = cv.convertScaleAbs(laplacian)

    cv.imshow('Laplacian', filtered_image)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()



# Supplementary - all
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    sobelxy = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelxy)

    edges = cv.Canny(image=gray, threshold1=100, threshold2=200)

    laplacian = cv.Laplacian(src=gray, ddepth=cv.CV_64F)
    filtered_image = cv.convertScaleAbs(laplacian)

    cv.imshow('Original', frame)
    cv.imshow('Sobel XY', filtered_image_xy)
    cv.imshow('Canny', edges)
    cv.imshow('Laplacian', filtered_image)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
