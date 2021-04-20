import cv2
import numpy as np
# 이미지의 경로
imageName = 'data/images/sample.jpg'

# opencv 로 이미지 열기

image = cv2.imread(imageName, cv2.IMREAD_COLOR)
image_gray = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
image_alpha = cv2.imread(imageName, cv2.IMREAD_UNCHANGED)

cv2.imshow('imgage_gray', image_gray)
cv2.imshow('image_alpha', image_alpha)


# 이미지가 정상인지 체크

if image is None :
    print('이미지 열수 없다.')

print(image)

print(image.shape)

# Gray Scale Image : RGB 3개가 아니라, 1개의 행렬로 만들고, 0~255까지의 숫자로 채워진
# 행렬로 변환한 이미지. ( 흑백이랑 다름 )

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 표시

cv2.imshow("image",image)     # 바로 종료되서 1초만에 이미지 사라짐
cv2.imshow("gray image", grayImage)
# cpu가 파일 자체를 실행해서, 끝냈기 때문에 imshow함수가 바로 종료됨
# 따라서, imshow 실행 후 눈으로 확인하기 위해서는 다음 코드로 작성

cv2.waitKey(0)  # cpu 가 종료하지 않고 기다림. 키 아무거나 누를때까지.
cv2.destroyAllWindow() # 누르면 , 프로그램을 종료




