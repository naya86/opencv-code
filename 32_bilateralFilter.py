## 선은 그대로 냅두고, 노이즈만 감소

import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

result = cv2.bilateralFilter(img, 15, 80, 80) # 8bit 1or 3채널 , 픽셀지름, color를 고려할 공간, 숫자크면 멀리있는 컬러 고려함

combined = np.hstack([img,result])

cv2.imshow('com', combined)


cv2.waitKey()
cv2.destroyAllWindows()