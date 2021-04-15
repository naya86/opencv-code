import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg', 1)

warpMat = np.float32( [1.2, 0.2, 2, -0.3, 1.3, 1] )

warpMat = warpMat.reshape(2,3)
# print(warpMat)
result = cv2.warpAffine( source, warpMat, ( int(source.shape[1] * 1.5), int( source.shape[0] * 1.5 ) ) )
#print(result)


cv2.imshow('original', source)
cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()



