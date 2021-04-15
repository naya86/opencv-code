import cv2

imageName = 'data/images/truth.png'

image =cv2.imread(imageName, 1)

cv2.imshow('original', image)

# 이미지의 경계를 깍아낸다  (erode)

dilationSize = 8

# 십자가모양
element = cv2.getStructuringElement( cv2.MORPH_CROSS, (2*dilationSize + 1, 2*dilationSize + 1), (dilationSize,dilationSize)  )

imageEroded = cv2.erode(image, element )

cv2.imshow('erosion', imageEroded)

#사각형모양
element1 = cv2.getStructuringElement( cv2.MORPH_RECT, (2*dilationSize + 1, 2*dilationSize + 1) )

imageEroded1 = cv2.erode(image,element1)

cv2.imshow('erosion1', imageEroded1)


cv2.waitKey()
cv2.destroyAllWindows()