import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

# 미디안블러 .. 노이즈 줄여준다. 점같은거 많이 퍼져있는 그런 이미지 필터링에 좋다.

# 3행3열 커널
dst1 = cv2.medianBlur(img, 5)   # 내부적으로 컨볼루션하고 돌려준다.    이미지, 커널사이즈 입력


# 13X13 커널

dst2 = cv2.medianBlur(img, 13)

combined = np.hstack([img, dst1, dst2])

cv2.imshow('com', combined)

cv2.waitKey()
cv2.destroyAllWindows()