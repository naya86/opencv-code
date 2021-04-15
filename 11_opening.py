import cv2

imageName = "data/images/opening.png"

image = cv2.imread(imageName, 0 )


cv2.imshow('original', image)

## opening    (이미지를 깍았다가 다시 확장시킴)

openingSize = 3

element = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (2*openingSize, 2*openingSize))  

imageOpened = cv2.morphologyEx( image, cv2.MORPH_OPEN, element, iterations=3  )# iteration  몇번 반복

cv2.imshow('opened', imageOpened)







cv2.waitKey()
cv2.destroyAllWindows()
