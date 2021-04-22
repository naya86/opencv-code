import cv2

# 바이너리   배경과 안에 내용만 가지고.

src = cv2.imread('data/images/threshold.png', 0 )

#구분하기 위한 값 설정
threshold = 50            # 0 은 숫자 0  까만색

# 위에서 설정한 값보다 큰 것들은, 모두 255로 색을 변경하겠다는 뜻

maxValue = 255

cv2.imshow('original',src)
ret, dst = cv2.threshold(src, threshold, maxValue, cv2.THRESH_BINARY )   #dst 는 적용된 이미지이다 (numpy)
ret, dst1 = cv2.threshold(src, threshold, maxValue, cv2.THRESH_BINARY_INV )
ret, dst2 = cv2.threshold(src, threshold, maxValue, cv2.THRESH_TRUNC )
ret, dst3 = cv2.threshold(src, threshold, maxValue, cv2.THRESH_TOZERO )
ret, dst4 = cv2.threshold(src, threshold, maxValue, cv2.THRESH_TOZERO_INV )


cv2.imshow('Thresholded BINARY', dst)
cv2.imshow('Thresholded BINARY_INV', dst)
cv2.imshow('Thresholded TRUNC', dst)
cv2.imshow('Thresholded TOZERO', dst)
cv2.imshow('Thresholded TOZERO_INV', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()