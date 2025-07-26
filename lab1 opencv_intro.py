# Example 1: read image
import cv2

img = cv2.imread(r"C:\Users\Zep\Downloads\Vargas.jpg", cv2.IMREAD_COLOR)

cv2.imshow(r"C:\Users\Zep\Downloads\Vargas.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Example 2: matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Zep\Downloads\Vargas.jpg")
plt.imshow(img)

plt.waitforbuttonpress()
plt.close ('all')



# Example 3: grayscale
import cv2

path = r"C:\Users\Zep\Downloads\Vargas.jpg"
img = cv2.imread (path, cv2. IMREAD_GRAYSCALE)

cv2.imshow(r"C:\Users\Zep\Downloads\Vargas.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Example 4: cam capture
import cv2

vid = cv2.VideoCapture(0)
while (True):

    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
