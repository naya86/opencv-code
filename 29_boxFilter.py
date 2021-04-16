import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

# 블러 .. 노이즈 줄여준다.

# 3행3열 커널
dst1 = cv2.blur(img, (3,3) )   # 내부적으로 컨볼루션하고 돌려준다.    이미지, 커널사이즈 입력


# 7X7 커널

dst2 = cv2.blur(img, (7,7) )

combined = np.hstack([img, dst1, dst2])

cv2.imshow('com', combined)

cv2.waitKey()
cv2.destroyAllWindows()