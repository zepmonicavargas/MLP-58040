# Averaging
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('banana.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur = cv.blur(img,(5,5))
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur_rgb),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()


# Gaussian Blur
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('banana.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur = cv.GaussianBlur(img,(5,5),200)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur_rgb),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()


# Median Blur
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('banana.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur = cv.medianBlur(img,25)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur_rgb),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()


# Bilateral Filtering
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('banana.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur = cv.bilateralFilter(img,12, 85, 85)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur_rgb),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()


# Supplementary: all with og and 2D conv filters
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('banana.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

blur = cv.blur(img_rgb,(5,5))
Gblur = cv.GaussianBlur(img_rgb,(5,5),200)
Mblur = cv.medianBlur(img_rgb,25)
Bblur = cv.bilateralFilter(img_rgb,12,85,85)
font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(blur,'Averaging',(100,300), font, 7, (255,0,0), 10)
cv.putText(Gblur,'Gaussian',(100,300), font, 7, (0,0,255), 10)
cv.putText(img_rgb,'Original',(200,300), font, 7, (0,0,0), 10)
cv.putText(Mblur,'Median',(250,300), font, 7, (0,255,200), 10)
cv.putText(Bblur,'Bilateral',(150,300), font, 7, (159,43,104), 10)

plt.subplot(331), plt.imshow(blur)
plt.xticks([]), plt.yticks([])
plt.subplot(333), plt.imshow(Gblur)
plt.xticks([]), plt.yticks([])

plt.subplot(335), plt.imshow(img_rgb)
plt.xticks([]), plt.yticks([])

plt.subplot(337), plt.imshow(Mblur)
plt.xticks([]), plt.yticks([])

plt.subplot(339), plt.imshow(Bblur)
plt.xticks([]), plt.yticks([])
plt.show()
