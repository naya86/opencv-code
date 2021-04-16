import cv2
import numpy as np

# 이미지의 밝기는 넓게 고루 펴준다.  이퀄라이져!


img = cv2.imread('data/images/candle.jpg')

ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

Ychannel, Cr, Cb = cv2.split(ycbImage)

print(Ychannel)

Ychannel = cv2.equalizeHist(Ychannel)    # 이 함수가 알아서 플롯갔다가 인트로 온다.

print(Ychannel)

ycbImage = cv2.merge( [ Ychannel, Cr, Cb ])

ycbImage = cv2.cvtColor( ycbImage, cv2.COLOR_YCrCb2BGR)

combined = np.hstack( [ img, ycbImage ] )

cv2.imshow('combined', combined)

cv2.waitKey()
cv2.destroyAllWindows()

