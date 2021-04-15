import cv2
import numpy as np

#캠으로부터 데이터 가져오기.

cap = cv2.VideoCapture(0)            # 경로대신에 숫자 0 , 연결된 캠이 숫자다. 하나면0 두개면 1 세개면 2 등등

if cap.isOpened() == False :
    print('Unable to read camera feed')

else :
    # 프레임 정보 가져오기 : 화면 크기 (width,height)
    frame_width = int(cap.get(3))   #  넓이가져오는거 3  
    frame_height = int(cap.get(4))  # 높이 가져오는거 4

    # 저장시키는 코드
    # 일을 하는 애를 먼저 만들고!!! (VideoWriter)
    out = cv2.VideoWriter('data/videos/output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height) )

    # 캠으로부터 사진을 계속 입력 받는다.
    while True :
        ret, frame = cap.read()



            # esc누르면 캠 꺼라
            if cv2.waitKey(1) & 0xFF == 27 :
                break  

        else :
            break
    
    cap.release()
    out.release()

    cv2.destroyAllWindows()