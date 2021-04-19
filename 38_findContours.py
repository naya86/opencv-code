# Contours 둘레.
# hough transform


import cv2
import numpy as np
import random


threshold = 0

maxthreshold = 255 * 3

random.seed(12345)

# 트랙바용 콜백 함수
def callback() :
    imCanny = cv2.Canny(img, threshold, threshold*2, apertureSize=3)

    # 컨투어스 시킨다. 엣지를 연결시킴
    contours, heirarchy = cv2.findContours(imCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 그린다.
    display = np.zeros( ( imCanny.shape[0], imCanny.shape[1] ) )

    for i in range(0, len(contours)) :
        lineColor = (255,0,0)
        cnt = contours[i]
        cv2.drawContours(display, [cnt], -1, lineColor, 2)

    cv2.imshow('Contours', display / 255.0)

# 쓰레숄드 조절 함수
def updateThreshold(*args) :
    global threshold
    threshold = args[0]
    callback()


img = cv2.imread('data/images/threshold.png', 0)

cv2.namedWindow('Contours', cv2.WINDOW_AUTOSIZE)

cv2.imshow('Contours', img)

cv2.createTrackbar('Canny and Contours', 'Contours', threshold, maxthreshold, updateThreshold)

callback()

cv2.waitKey()
cv2.destroyAllWindows()