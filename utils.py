import cv2
import numpy as np

# 마우스로 클릭하여 점 만드는 함수

def mouse_handler(event, x, y, flasgs, data) :
    
    if event == cv2.EVENT_LBUTTONDOWN : # 마우스 왼쪽 클릭
        cv2.circle(data['im'], (x,y), 3, (0,0,255) )
        cv2.imshow('image', data['im'] )
        
        if len(data['points']) < 4 :
            data['points'].append( [ x,y ] )


def get_four_points(im) :
    data = {}
    data['im'] = im.copy()
    data['points'] = []

    cv2.imshow('image', im)
    cv2.setMouseCallback('image', mouse_handler, data)
    cv2.waitKey()

    # 유저가 마우스로 찍은 점을 float으로 바꿔줘야한다.
    points = np.array(data['points'], dtype=float)
    
    return points