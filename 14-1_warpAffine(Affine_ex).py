import cv2
import numpy as np

## Affine Transform 예제
img = cv2.imread('data/images/sample.jpg')
# print(img)
rows, cols, ch = img.shape

pts1 = np.float32([[200,100],[400,100],[200,200]])
pts2 = np.float32([[200,300],[400,200],[200,400]])


# pts1의 좌표를 이미지에 표시한다.변환 후 점 확인
cv2.circle(img, (200,100), 10, (255,0,0),-1)
cv2.circle(img, (400,100), 10, (0,255,0),-1)
cv2.circle(img, (200,200), 10, (0,0,255),-1)


M = cv2.getAffineTransform(pts1, pts2)


dst = cv2.warpAffine(img, M, (cols,rows))


cv2.imshow('ori', img)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()