import cv2
import numpy as np

## 색감 바꿨다!

src = cv2.imread('data/images/image1.jpg')
dst = cv2.imread('data/images/image2.jpg')

cv2.imshow('src', src)
cv2.imshow('dst', dst)

output = dst.copy()  #  이미지 하나 더 만들기

srcLab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
dstLab = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB)
outputLab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)

# 연산 쉽게 하기위해 float

srcLab = srcLab.astype('float')
dstLab = dstLab.astype('float')
output = np.float32(outputLab)

#print(srcLab)

#채널 분리  (LAB)
srcL, srcA, srcB = cv2.split(srcLab)
dstL, dstA, dstB = cv2.split(dstLab)
outL, outA, outB = cv2.split(outputLab)
#1차 연산
outL = dstL - dstL.mean()
outA = dstA - dstA.mean()
outB = dstB - dstB.mean()

# 우리가 얻고자하는 이미지
outL = outL * ( srcL.std() / dstL.std() )
outA = outA * ( srcA.std() / dstA.std() )
outB = outB * ( srcB.std() / dstB.std() )

outL = outL + srcL.mean()
outA = outA + srcA.mean()
outB = outB + srcB.mean()

# 우리가 눈으로 보기 위해서는 ? 사진은 0~255사이값으로 세팅

outL = np.clip(outL, 0, 255)
outA = np.clip(outA, 0, 255)
outB = np.clip(outB, 0, 255)

#채널 합치기
outputLab = cv2.merge( [ outL, outA, outB ] )

#이미지는 8비트 정수이므로, 형 변환해준다.

outputLab = np.uint8(outputLab)

# imshow는 BGR이므로 , 
outputLab = cv2.cvtColor( outputLab, cv2.COLOR_LAB2BGR)

cv2.imshow("output", outputLab)



cv2.waitKey()
cv2.destroyAllWindows()
