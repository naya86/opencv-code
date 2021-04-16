import cv2
import numpy as np

# 두개의 사진 가지고 같은 방향으로 맞추기
# 네개의 점이 필요

# 첫번째 이미지.
img_src = cv2.imread('data/images/book2.jpg')

point_src = np.array( [ 141,131, 480,159, 493,630, 64,601 ],dtype=float)

point_src = point_src.reshape(4,2)

print(point_src)

# 두번째 이미지.

img_dst = cv2.imread('data/images/book1.jpg')

point_dst = np.array( [ 318,256, 534,372, 316,670, 73,473 ], dtype=float )

point_dst = point_dst.reshape(4,2)

print(point_dst)

# 호모그라피에서 변환된 행렬 찾기
# h가 변환에 이용된 바로, 3 X 3 의 행렬이다.
h, status = cv2.findHomography(point_src, point_dst)

img_output = cv2.warpPerspective(img_src, h, (img_src.shape[1], img_src.shape[0]))

cv2.imshow('SRC', img_src)
cv2.imshow('DST', img_dst)
cv2.imshow('Warp', img_output)

cv2.waitKey()
cv2.destroyAllWindows()


