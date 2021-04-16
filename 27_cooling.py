import cv2
import numpy as np


# 이미지를 차갑게만드는  ! 

original = cv2.imread('data/images/girl.jpg')

img = original.copy()


# x축 피봇 포인트
originalValue = np.array( [ 0, 50, 100, 150, 200, 255 ] )

# y축 (CrCd)포인트 : 빨간쪽, 파란쪽 두 부분의 포인트

bCurve = np.array( [ 0, 80, 150, 190, 220, 255 ] )
rCurve = np.array( [ 0, 20, 40, 75, 150, 255 ] )


#Lookup 테이블 만들기

fullrange = np.arange(0, 255+1)

rLUT = np.interp(fullrange, originalValue, rCurve)

print(rLUT)

bLUT = np.interp(fullrange, originalValue, bCurve)

print(rLUT)

rChannel = img[ : ,  : , 2]  #   3차원 #split 하고 똑같음.

rChannel = cv2.LUT(rChannel, rLUT)

img[ : , :, 2] = rChannel


bChannel = img[ : , : , 0] 
bChannel = cv2.LUT(bChannel, bLUT)

img[ : , : , 0 ] = bChannel

combined = np.hstack([ original, img ])

cv2.imshow("com", combined)

cv2.waitKey()
cv2.destroyAllWindows()
