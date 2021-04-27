import cv2
import numpy as np

# translation
img = cv2.imread('data/images/sample.jpg')

rows, cols = img.shape[:2]
print(img.shape)
print(cols)

# 변환 행렬, X축으로 10, Y축으로 20 이동
M = np.float32([[1,0,10],[0,1,20]])

dst = cv2.warpAffine(img, M,(cols, rows))
cv2.imshow('Original', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()






# 어파인
source = cv2.imread('data/images/sample.jpg', 1)

warpMat = np.float32( [1.2, 0.2, 2, -0.3, 1.3, 1] )

warpMat = warpMat.reshape(2,3)
print(warpMat)
result = cv2.warpAffine( source, warpMat, ( int(source.shape[1] * 1.5), int( source.shape[0] * 1.5 ) ) )
print(result)


cv2.imshow('original', source)
cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()



