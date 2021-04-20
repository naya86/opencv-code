import cv2
# crop은 이미지의 특정 부분만 가져옴

source = cv2.imread('data/images/sample.jpg',1) # 02파일에는 cv2.IMREAD_COLOR로 되어있음.
# source = cv2.imread('data/images/sample.jpg',2) # 02파일에는 cv2.IMREAD_COLOR로 되어있음.
# source = cv2.imread('data/images/sample.jpg',3) # 02파일에는 cv2.IMREAD_COLOR로 되어있음.
print(source.shape)
# 이미지 확대 축소
# 1은 100% , 0.6은 60% , 1.8은 180% 확대 / 축소 가능
scaleX = 0.6
scaleY = 0.6

scaleDown = cv2.resize(source,None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

scaleX = 1.8
scaleY = 1.8

scaleUp = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)


cv2.imshow('original', source)
cv2.imshow('scaleDown',scaleDown )
print(scaleDown.shape)
cv2.imshow('scaleUp', scaleUp)
print(scaleUp.shape)

# 내가 원하는 부분의 이미지를 가져오기 (crop)

crop_img = source[ 100:200 , 150 :250] # x축 150부터 250 , y축 100부터 200
 # 넘파이의 행렬과 이미지의 행렬은 반대 개념. x축 y축             #넘파이의 행은 y값, 열은 x값

# crop_img2 = source[ 100:200 ][150 :250]   # crop img2 사용금지
print(crop_img.shape)
cv2.imshow('Cropped Img', crop_img)
# cv2.imshow('Cropped Img', crop_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


