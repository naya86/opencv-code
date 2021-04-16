import cv2
import numpy as np

## 감마 조절 (디지털을 사람의 눈으로 본것처럼 조절)

img = cv2.imread('data/images/candle.jpg', 1)

gamma = 2.5

fullRange = np.arange(0,256)

lookupTable = np.uint8( 255 * np.power( (fullRange / 255.0 ) , gamma ) )

#감마값 조정 함수
output = cv2.LUT(img, lookupTable)

combined = np.hstack([img, output])

cv2.imshow('com', combined)

cv2.waitKey()

cv2.destroyAllWindows()