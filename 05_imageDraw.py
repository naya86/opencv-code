import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image)
print(image.shape)

# 선 그리기

imageLine = image.copy()  #  이미지 카피

cv2.line(imageLine, (322,179), (400,183), (0,255,0), thickness=2, lineType=cv2.LINE_AA)   # 선의 시작점 , 끝점,  선색깔(BGR)  , thickness는 선두께  ,  라인타입
cv2.imshow('image line', imageLine)

# 원 그리기

imageCircle = image.copy()

cv2.circle(imageCircle,(350,200), 150, (255,0,0), thickness=3, lineType=cv2.LINE_AA)  # 원의 중심  ,  간격, 색 , 두께 , 라인타입
cv2.imshow('image circle', imageCircle)

# 타원그리기

imageELLipse = image.copy()

cv2.ellipse(imageELLipse, (360,200), (100,170), 45, 0, 360, (0,255,0),thickness=2)
cv2.ellipse(imageELLipse, (360,200), (100,170),135, 0, 360, (0,0,255),thickness=2)
cv2.imshow('image ellipse', imageELLipse)


# 사격형 그리기    # 영역표시 탁월

imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (208,55), (450,355), (255,0,0), thickness=3) #왼쪽윗모서리, 오른쪽 아래 모서리
cv2.imshow('rectangle', imageRectangle)

# 글자 넣기

imageText = image.copy()
cv2.putText(imageText, 'Mark Zuckerberg', (205,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2 ) #  파라미터는 다 레퍼런스 참고..
cv2.imshow('text', imageText)

# 사각형 + 글자넣기
imageMulty = image.copy()
cv2.rectangle(imageMulty, (208,55), (450,355), (255,0,0), thickness=3)
cv2.putText(imageMulty, 'Mark Zuckerberg', (205,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2 )
cv2.imshow('multiple', imageMulty)



cv2.waitKey(0)
cv2.destroyAllWindows()



