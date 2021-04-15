import cv2

imageName = "data/images/closing.png"

image = cv2.imread(imageName, 0 )


cv2.imshow('original', image)

## closing    (이미지를 확장 다시 침식시킴)

closingSize = 3

element = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (2*closingSize, 2*closingSize))  

imageClosed = cv2.morphologyEx( image, cv2.MORPH_CLOSE, element, iterations=3  )# iteration  몇번 반복

cv2.imshow('Closed', imageClosed)







cv2.waitKey()
cv2.destroyAllWindows()