import cv2
import numpy as np
from utils import get_four_points


img_src = cv2.imread('data/images/first-image.jpg',1)

img_dst = cv2.imread('data/images/times-square.jpg',1)

dst_size = img_dst.shape

# img_dst = np.zeros(dst_size, np.uint8)  # 빈 행렬만들기. 0

# cv2.imshow('dst', img_dst)


# 우리가 원본이미지로부터 4개의 점을 바로 가져온다.

cv2.imshow('src image', img_src)

points_src = np.array( [ 0,0, 
                        img_src.shape[1],0, 
                        img_src.shape[1],img_src.shape[0], 
                        0,img_src.shape[0] ])

points_src = points_src.reshape(4,2)

# 새로만들 이미지에서는, 위의 원본 이미지 4개의 점을 마우스로 구한다.

# cv2.imshow('dst image',img_dst)

points_dst = get_four_points(img_dst)

h, status = cv2.findHomography(points_src, points_dst)

img_temp = cv2.warpPerspective(img_src, h, (dst_size[1],dst_size[0]) )

cv2.imshow('temp',img_temp)


# 타임스퀘어의 전광판  안쪽을 0 으로 바꿔준다.
cv2.fillConvexPoly(img_dst, points_dst.astype(int), 0) 

cv2.imshow("img to 0", img_dst)

# 두개 더함
img_result = img_dst + img_temp
cv2.imshow('result', img_result)


cv2.waitKey()
cv2.destroyAllWindows()