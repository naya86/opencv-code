import cv2
import numpy as np

# 원본이미지와 변환된 이미지 가지고, 변환에 사용된 행렬 구하기
input_tri = np.float32( [ 50,50, 100,100, 200,150 ] )

#삼각형 세 점 좌표로 변환.
input_tri = input_tri.reshape(3,2)

#변환된 이미지의 세 점이 좌표
ouput_tri = np.float32( [ 70,76, 142, 101, 272, 136 ] ) 

#세점의 좌표로 변환
ouput_tri = ouput_tri.reshape(3,2)

print(input_tri)
print(ouput_tri)

# 변환에 사용된 행렬 구하기.
warpMat = cv2.getAffineTransform(input_tri,ouput_tri)
print(warpMat)


