import cv2
import numpy as np

img= cv2.imread('data/images/truth.png', 1)

sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0 ) # sobel필터   # x축엣지. 수직선
sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1 ) #y축엣지 수평선


cv2.imshow('ori', img)
cv2.imshow('sobel X', sobelx)
cv2.imshow('sobel Y', sobely)

cv2.waitKey()
cv2.destroyAllWindows()

## 노이즈가 많으면 엣지를 찾을 수가 없다.