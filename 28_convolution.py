import cv2
import numpy as np

##  컨볼루션 기능

img = cv2.imread('data/images/gaussian-noise.png', 1)

# cv2.imshow('img', img)

kernel_size = 5   # 행과열이 같음

kernel = np.ones( ( kernel_size, kernel_size ) ) / kernel_size**2

# print(kernel)

#컨볼루션
result = cv2.filter2D( img, -1, kernel ) # 입력 영상, 출력영상 데이터타입(-1은 같은타입), 필터마스크 행렬

combined = np.hstack( [img, result])

cv2.imshow('com', combined)


cv2.waitKey()
cv2.destroyAllWindows()



