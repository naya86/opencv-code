import numpy as np
import argparse
import imutils
import time
import cv2
import os
import matplotlib.pyplot as plt

DEFAULT_FRAME = 1
SET_WIDTH = int(600)

sv = cv2.VideoCapture('data4/video/dashcam2.mp4')
sample_video_writer = None
#모델 가져오기
cv_enet_model = cv2.dnn.readNet('data4/enet-cityscapes/enet-model.net')

#색정보 가져오기
CV_ENET_SHAPE_IMG_COLORS = open('data4/enet-cityscapes/enet-colors.txt').read().split('\n')
CV_ENET_SHAPE_IMG_COLORS = CV_ENET_SHAPE_IMG_COLORS[  :  -2+1]
CV_ENET_SHAPE_IMG_COLORS = np.array([np.array(color.split(',')).astype('int')  for color in CV_ENET_SHAPE_IMG_COLORS  ])

try : 
    prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() else cv2.CAP_PROP_FRAME_COUNT
    total = sv.get(prop)
    print('[INFO]{} total frames in video.'.format(total))
except :
    print("[INGO] could not determine number of frames in video")
    total = -1

while True :
    grabbed, frame = sv.read()

    if grabbed == False :
        break
    
    normalize_image = 1 / 255.0
    resize_image_shape = (1024,512)
    
    video_frame = imutils.resize( frame, width= SET_WIDTH )
    blob_img = cv2.dnn.blobFromImage( frame, normalize_image, resize_image_shape, 0, swapRB= True, crop = False)
    
    cv_enet_model.setInput(blob_img)
    # 모델이 세그멘테이션 추론하는데 얼마나 걸리는지 측정
    start_time = time.time()
    cv_enet_model_output = cv_enet_model.forward()
    end_time = time.time()

    print(end_time - start_time)
    
    (classes_num, height, width) = cv_enet_model_output.shape[1:4]

    class_map = np.argmax(cv_enet_model_output[0],axis=0 )

    mask_class_map = CV_ENET_SHAPE_IMG_COLORS[class_map]# 3차원

    mask_class_map = cv2.resize(mask_class_map, (video_frame.shape[1], video_frame.shape[0]), interpolation = cv2.INTER_NEAREST)

    cv_enet_model_output = ( (0.3 * video_frame) + (0.7 * mask_class_map) ).astype('uint8')

    # print(cv_enet_model_output)

    cv2.imshow("Frame", cv_enet_model_output)     #  가공이 필요할때는 이 부분에 가공을 해주면 된다.

    #키보드에서 esc키를 누르면 exit 하라
    if cv2.waitKey(25) & 0xFF == 27 :
        break

sv.release()  # 비디오파일 닫는 느낌

cv2.destroyAllWindows()
    

