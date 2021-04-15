import cv2
import numpy as np

# FPS : Frame per Second : 1초당 몇장의 사진으로 구성되어있나.

# 비디오 파일에서 읽어오기.

cap = cv2.VideoCapture('data/videos/chaplin.mp4')

if cap.isOpened() == False :                   # True False로 값이 나옴 isOpened
    print('Error opening video stream of file')

else :
    # 반복문 필요이유 : 비디오는 여러 사진으로 구성되어 있으니까.! 여러개니까
    while cap.isOpened() :
        
        # 사진을 한장씩 가져와서 

        ret, frame = cap.read()       # ret 에는 True , False 로 가져오고 , frame 에는 numpy 로 가져옴(이미지). 비디오에 관한 프레임이 있으면 ret은 True

        # 제대로 사진 가져왔으면, 화면에 표시
        if ret == True :
            cv2.imshow("Frame", frame)           #  가공이 필요할때는 이 부분에 가공을 해주면 된다.

            #키보드에서 esc키를 누르면 exit 하라
            if cv2.waitKey(25) & 0xFF == 27 :
                break

        else : 
            break

cap.release()  # 비디오파일 닫는 느낌

cv2.destroyAllWindows()