import cv2

source = cv2.imread('data/images/sample.jpg', 1)

# rotate는 이미지를 회전시킨다.

# 회원의 중심좌표 

center = ( source.shape[1] / 2, source.shape[0] / 2 )  # 넘파이라 가능 넘파이의 행은 y축, 열(컬럼)은 x축
#각도
rotationAngle = 50
#이미지 확대 및 축소
scaleFactor = 1

# 아래는 행렬로 나온다.
rotationMatrix = cv2.getRotationMatrix2D( center, rotationAngle,scaleFactor )# 중심점, 각도, 확대축소파라미터(1이상은 확대)
print(rotationMatrix.shape)

# rotate 
result = cv2.warpAffine( source, rotationMatrix, ( source.shape[1], source.shape[0] ) )
# * cv2.warpAffine( src, M, dsize )
# - src : 변환할 이미지- M : 변환행렬
# - dsize : output image size (ex; (width=columns, height=rows)

cv2.imshow('original', source)
cv2.imshow('rotated', result)

cv2.waitKey()
cv2.destroyAllWindows()