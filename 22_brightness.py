import cv2
import numpy as np


img = cv2.imread('data/images/candle.jpg', 1)

beta = 150

## Ycrcb   

# 컬러스페이스 변경
ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# 가공 위한 unit8 을 플롯으로

ycbImage = np.float32(ycbImage)

#채널분리

Ychannel, Cr, Cb = cv2.split(ycbImage)


#밝기조절
Ychannel = np.clip( Ychannel + beta, 0, 255 )

# 채널 합치기

ycbImage = cv2.merge( [ Ychannel, Cr, Cb] ) 

# 다시 unit8로 변경
ycbImage = np.uint8(ycbImage)

# 화면 표시 위해서 컬러스페이스 BGR로 변경
ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', img)
cv2.imshow('dst', ycbImage)

# 아래는 하나의 윈도우에 , 2개의 이미지를 옆으로 붙여서 표시.

img_all = np.hstack( [ img, ycbImage ] )
cv2.imshow('all', img_all)

cv2.waitKey()
cv2.destroyAllWindows()

