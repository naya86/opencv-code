# 차선 인식 

import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


# 칼라이미지.
image_color = cv2.imread('data2/image.jpg')
#cv2.imshow('ori', image_color)


# 우리가 필요한건 그레이 스케일
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', image_gray)


image_copy = image_gray.copy()

# 값이 195 미만인것들은 0으로 셋팅 (까맣게)
#print(image_copy.shape)

print(image_copy[ : , : ] < 195)

image_copy[ image_copy[ : , : ] < 195 ] = 0

#cv2.imshow('copy', image_copy)


image = cv2.imread('data2/test_image.jpg')
print('height= ', int(image.shape[0]), 'pixels')
print('width =', int(image.shape[1]), 'pixels')

# cv2.imshow('Self Driving Car!', image)

# 그레이로 바꿔보자

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('SDC Gray', gray_img)   # 그레이는 2차원, 컬러는 3차원

# HSV 컬러 스페이스로 변경
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # openCV 는 BGR로 보여서 이상함.
# HSV 는 RGB임
#cv2.imshow('HSV', hsv_image)

# Hue 채널만 표시 (HSV)
H, S, V = cv2.split(hsv_image)  # 채널 나누기

# 다른 방법 np.array ( hsv_image[ : , : , 0 ] ) 원래 넘파이임. H

#cv2.imshow("Hue", H)    #imshow 는 BGR 로 화면에 표시 채널이 하나면 그레이스케일로 표시됨


# 엣지 선명하게!
# Shapenning   1
# 가운데 부분을 크게 써준다. 클수록 엣지가 강하다.
sharp_kernel_1  = np.array( [

    [0,-1,0],
    [-1,5,-1],                   
    [0,-1,0]
] )

sharpened_img_1 = cv2.filter2D(gray_img, -1, sharp_kernel_1)
# cv2.imshow('gray', gray_img)
# cv2.imshow('Sharpen', sharpened_img_1)


# Shapenning   2
sharp_kernel_2  = np.array( [

    [0,-1,0],
    [-1,9,-1],                   
    [0,-1,0]
] )

sharpened_img_2 = cv2.filter2D(gray_img, -1, sharp_kernel_2)
#cv2.imshow('Sharpen2', sharpened_img_2)




# 노이즈 감소 블러링

blur_img = cv2.GaussianBlur( gray_img, (5,5), 10 )
#cv2.imshow('blur', blur_img)



# Sobel Edge detection
x_sobel= cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=7)
#cv2.imshow('sobel x', x_sobel)   #수평선

y_sobel= cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=7)
#cv2.imshow('sobel y', y_sobel)   # 수직선




# Laplacian 한번에 수직수평 다 잡음  ( 노이즈 부분도 다 나옴 )

laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
#cv2.imshow('laplacian', laplacian)


# Canny edge detection
threshold_1 = 120
threshold_2 = 200

canny_img = cv2.Canny(gray_img, threshold_1, threshold_2 )
#cv2.imshow('canny', canny_img)


# image transformation   ( 이미지 회전 )

image = cv2.imread('data2/test_image2.jpg')
#cv2.imshow('ori', image)
#print(image.shape)  # 464,664,3

# 센터중심 회전
                                         # width             #height
M_rotation = cv2.getRotationMatrix2D( ( image.shape[1] / 2, image.shape[0] / 2 ), 90, 0.5 ) # 중심점, 각도, 확대(축소)
# 행렬도 결과값이 나옴 위에꺼
rotated_img = cv2.warpAffine(image, M_rotation, (image.shape[1], image.shape[0]) )
#cv2.imshow('rotated', rotated_img)



# image translation ( 이미지 이동 )

image = cv2.imread('data2/test_image3.jpg')
#cv2.imshow('ori', image)

height = image.shape[0]
width = image.shape[1]

T_matrix = np.array( [ 
    [1, 0, 120],    # 대각선 1,0,0,1 회전을 시키지 않고, 120, -150 이동만 시켜라.
    [0, 1, -150]
], dtype='float32' )

#print(T_matrix)

translation_image = cv2.warpAffine(image, T_matrix, (width, height))
#cv2.imshow('trans', translation_image)


# image resizing ( 이미지 사이즈 변경 )

resized_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)   # x축으로 몇배, y축으로 몇배
                                     #확대 축소시 중간에 비는 거 처리
#cv2.imshow('resize', resized_image)


# Region of interest masking ( 관심 영역 마스킹 )
# RoI : 관심영역

image_color = cv2.imread('data2/test5.jpg')

image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

#cv2.imshow('gray', image_gray)

print(image_gray.shape)
# 관심영역에 점 4개 찍어주기

# np.zeros함수는 파라미터로, 몇행몇열로 만들지 넣어줘야한다.
# blank = np.zeros( ( image_gray.shape[0], image_gray.shape[1] ) )
blank = np.zeros_like(image_gray)

print(blank.shape)

ROI = np.array( [ [ (0,400), (300,250), (450,300), (700,426) ]  ],dtype=np.int32 ) #좌표는 2차원

mask = cv2.fillPoly(blank, ROI, 255) # blank 자체를 변형시킨다 . mask로
print(mask)


# cv2.imshow('blank',blank)
# cv2.imshow('mask', mask)

masked_image = cv2.bitwise_and(image_gray, mask)
#cv2.imshow('masked', masked_image)


# hough transform
# 누락되거나, 깨진 영역을 복원
image_c = cv2.imread('data2/calendar.jpg')
image_g = cv2.cvtColor(image_c, cv2.COLOR_BGR2GRAY)

image_canny = cv2.Canny(image_g, 50, 200, apertureSize = 3 )
#cv2.imshow('Canny', image_canny)  # 연결 안된 부분이 있음.

lines = cv2.HoughLines(image_canny, 1, np.pi / 180, 250)

for i in range(len(lines)):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 -1000*(a))

        cv2.line(image_c,(x1,y1),(x2,y2),(255,0,0),2)
cv2.imshow('Canny', image_c)

cv2.waitKey()
cv2.destroyAllWindows()
