# 캐니 엣지 업그레이드 버전
# 엣지 가장 잘 잡는 쓰레숄드 찾기
import cv2
import numpy as np 

highThreshold = 100
lowThreshold = 50

maxThreshold = 1000

apertureSizes = [ 3, 5, 7 ]   # 조리개 사이즈
maxapertureIndex = 2 # 위의 숫자 몇개?  0부터

apertureIndex = 0  # 0부터

blurAmount = 0
maxBlurAmount = 20

# 트랙바용 함수

# 캐니엣지 적용하는 함수
def applyCanny():
    if blurAmount > 0 :  # 블러값이 있으면
        blurredSrc = cv2.GaussianBlur(src, (2*blurAmount +1, 2*blurAmount +1), 0 )
    else :
        blurredSrc = src.copy()

    apertureSize = apertureSizes[apertureIndex]

    edges = cv2.Canny(blurredSrc, lowThreshold, highThreshold, apertureSize=apertureSize)

    cv2.imshow('Edges', edges)    

# 로우 쓰레숄드 적용하는 함수
def updateLowThreshold(*args) : # 파라미터를 리스트로 받겠다.
    global lowThreshold
    lowThreshold = args[0]
    applyCanny()

# 하이 쓰레숄드 적용하는 함수
def updateHighThreshold(*args) :
    global highThreshold
    highThreshold = args[0]
    applyCanny()

# 블러 적용하는 함수
def updateBlurAmount(*args) :
    global blurAmount
    blurAmount = args[0]
    applyCanny()

# aperture 적용하는 함수
def updateApertureIndex(*args) :
    global apertureIndex
    apertureIndex = args[0]
    applyCanny()


src = cv2.imread('data/images/sample.jpg', 0)

edges = src.copy()

cv2.imshow('Edges', src)

cv2.namedWindow('Edges', cv2.WINDOW_AUTOSIZE)

# 로우 쓰레숄드에 대한 컨트롤러 트랙바에 붙인다.
cv2.createTrackbar('Low Threshold', 'Edges', lowThreshold, maxThreshold, updateLowThreshold)


# 하이 쓰레숄드에 대한 컨트롤러 트랙바에 붙인다.
cv2.createTrackbar('High Threshold', 'Edges', highThreshold, maxThreshold, updateHighThreshold)

# aperture를 트랙바에 붙인다.
cv2.createTrackbar('Aperture Size', 'Edges', apertureIndex, maxapertureIndex, updateApertureIndex)

# blur를 트랙바에 붙인다.
cv2.createTrackbar('Blur', 'Edges', blurAmount, maxBlurAmount, updateBlurAmount)

cv2.waitKey()
cv2.destroyAllWindows()