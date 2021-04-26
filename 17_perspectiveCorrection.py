import cv2
import numpy as np
from utils import get_four_points

img_src = cv2.imread('data/images/book1.jpg')

# 결과물 이미지 사이즈 
dst_size = (400, 300, 3)

# 결과의 이미지를 넣을 행렬 , 0행렬
img_dst = np.zeros(dst_size, np.uint8)  # 빈 행렬만들기. 0

#cv2.imshow('dst', img_dst)



# 우리가 원본이미지로부터는 마우스 클릭으로 4개의 점을 가져온다.
# 새로만들 이미지에서는, 위의 원본 이미지 4개의 점과 매핑할 점을 잡아줘야한다.

# cv2.imshow('image',img_src)

# 함수를 호출하여 이미지 작업한다.
points_src = get_four_points(img_src)

points_dst = np.array([ 0,0, dst_size[1],0, 
            dst_size[1],dst_size[0], 0,dst_size[0] ], dtype=float)

points_dst = points_dst.reshape(4,2)
print(points_dst)

h, status = cv2.findHomography(points_src, points_dst)

img_dst = cv2.warpPerspective(img_src, h, (dst_size[1],dst_size[0]) )

cv2.imshow('result',img_dst)

cv2.waitKey()
cv2.destroyAllWindows()






# ## 내 사진으로 해보기


# img_src = cv2.imread('data/images/me.jpg')

# dst_size = (400, 300, 3)

# img_dst = np.zeros(dst_size, np.uint8)  # 빈 행렬만들기. 0

# #cv2.imshow('dst', img_dst)



# # 우리가 원본이미지로부터는 마우스 클릭으로 4개의 점을 가져온다.
# # 새로만들 이미지에서는, 위의 원본 이미지 4개의 점과 매핑할 점을 잡아줘야하낟.

# cv2.imshow('image',img_src)
# points_src = get_four_points(img_src)

# points_dst = np.array([ 0,0, dst_size[1],0, 
#             dst_size[1],dst_size[0], 0,dst_size[0] ], dtype=float)

# points_dst = points_dst.reshape(4,2)

# h, status = cv2.findHomography(points_src, points_dst)

# img_dst = cv2.warpPerspective(img_src, h, (dst_size[1],dst_size[0]) )

# cv2.imshow('aa',img_dst)

# cv2.waitKey()
# cv2.destroyAllWindows()
