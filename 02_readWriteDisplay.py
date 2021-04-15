import cv2

imageName = 'data/images/sample.jpg'

image = cv2.imread( imageName, cv2.IMREAD_COLOR)

if image is None:
    print("Could not open or find the image")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 창에 이름과 성질을 설정
cv2.namedWindow('gray image', cv2.WINDOW_AUTOSIZE)

#위에서 설정한 창 gray image에다, numpy 인 grayimage를 표현
cv2.imshow('gray image', grayImage)

# 작업한 이미지를 파일로 저장하는 코드
cv2.imwrite('data/images/result_gray.jpg', grayImage)

cv2.waitKey(0)
cv2.destroyAllWindow()