## 이미지를 날카롭게 만든후 엣지를 찾아서 큰 쓰레숄더(색변화가 큰거)와 작은 쓰레숄더를 적용해, 
## 연결한다.
## 캐니엣지는 그레이스케일을 이용한다.

import cv2
import numpy as np

img = cv2.imread('data/images/sample.jpg', 0)

cv2.imshow('gray', img)

# 하이쓰레숄드
threshold_1 = 120
# 로우쓰레숄드
threshold_2 = 200

result = cv2.Canny(img, threshold_1, threshold_2)

cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()


