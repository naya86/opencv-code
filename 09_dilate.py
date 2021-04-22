import cv2

# 바이너리   배경과 안에 내용만 가지고.
imageName = 'data/images/truth.png'

image =cv2.imread(imageName, 0)

cv2.imshow('original', image)


# 이미지의 경계 부분을 확장  ( dilation )

dilationSize = 10

# 십자가모양
element = cv2.getStructuringElement( cv2.MORPH_CROSS, (2*dilationSize + 1, 2*dilationSize + 1), (dilationSize,dilationSize)  )

imageDilate = cv2.dilate(image,element)

cv2.imshow('Dilation', imageDilate)

#사각형모양
element1 = cv2.getStructuringElement( cv2.MORPH_RECT, (2*dilationSize + 1, 2*dilationSize + 1) )

imageDilate1 = cv2.dilate(image,element1)

cv2.imshow('Dilation1', imageDilate1)


cv2.waitKey()
cv2.destroyAllWindows()