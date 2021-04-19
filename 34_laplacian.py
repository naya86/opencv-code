# 가우시안 블러를 먼저 미분해서 , 필터링하고, 다시한번 2차 미분을 하는 
# 엣지디텍터

import cv2
import numpy as np

img = cv2.imread('data/images/truth.png', 1)

laplacian = cv2.Laplacian(img, cv2.CV_32F, ksize=3, scale=1) # 3행3열 커널 

cv2.imshow('ori', img)
cv2.imshow('laplacian', laplacian)

cv2.waitKey()
cv2.destroyAllWindows()