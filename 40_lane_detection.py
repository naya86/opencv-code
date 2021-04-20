import cv2
import numpy as np

# 레인 디텍션

# # 1. 이미지 불러오기 . 

# image = cv2.imread('data3/test_image.jpg')
# cv2.imshow('ori', image)

# # 2. 이미지 그레이스케일
# lanelines_image = image.copy()
# gray_conversion = cv2.cvtColor(lanelines_image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray_conversion)

# # 3. 이미지 스무딩 ( 가우시안 )
# #내가 한거
# #bilateral = cv2.bilateralFilter(gray_conversion, 15, 80, 80)
# #cv2.imshow('bi', bilateral)

# blur_conversion = cv2.GaussianBlur(gray_conversion,(5,5), 0)
# cv2.imshow('smooth', blur_conversion)

# # 4. 캐니엣지 디텍션

# canny_conversion = cv2.Canny(blur_conversion, 50, 155)
# cv2.imshow('canny', canny_conversion)


# 2, 3, 4 순서도 함수로 만든다.

def canny_edge(image) :
    gray_conversion = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_conversion = cv2.GaussianBlur(gray_conversion, (5,5), 0)
    canny_conversion = cv2.Canny(blur_conversion, 50, 150)
    return canny_conversion



# 5. 마스킹 레전 오브 인터레스트 ,  ROI (함수로 만들기)

def reg_of_interest(image) :
    image_height = image.shape[0]
    polygons = np.array( [ [ (200, image_height), (1100,image_height),(550,250) ] ] )#삼각형
    image_mask = np.zeros_like(image)
    cv2.fillPoly(image_mask, polygons, 255) # image_mask 바로 저장
    masking_image = cv2.bitwise_and(image, image_mask)
    return masking_image

# 가져온 라인을 가져와라 (함수)

def show_lines(image, lines) :
    lines_image = np.zeros_like(image)
    if lines is not None :
       for i in range(len(lines)):
            for x1,y1,x2,y2 in lines[i]:
                cv2.line(lines_image,(x1,y1),(x2,y2),(255,0,0),10)  
    return lines_image      


# 기울기와 y절편 평균화 함수 ( 여러선을 하나의 선으로 만들어 주는 함수 )
# 좌표 변환
def make_cordinates(image, line_parameters) :
    slope, intercept = line_parameters   #slope 기울기 , intercept y 절편
    y1 = image.shape[0]
    y2 = int(y1* (1/2) )  #  괄호안 숫자가 라인 길이.
    x1 = int( (y1-intercept)/ slope)
    x2 = int( (y2- intercept)/ slope)
    return np.array( [x1,y1,x2,y2] )
# 평균 구하기
def average_slope_intercept(image, lines) :
    left_fit = []
    right_fit = []
    for line in lines : #허프에서 넘어온 라인
        x1, y1, x2, y2 = line.reshape(4)
        # 직선의 기울기와 y절편을 가져올 수 있다.
        parameter = np.polyfit( (x1,x2), (y1,y2), 1 )
        slope = parameter[0]
        intercept = parameter[1]
        if slope < 0 :    
            left_fit.append( (slope, intercept) )
        else : 
            right_fit.append( (slope, intercept) )
    left_fit_average = np.average(left_fit, axis=0)                    
    right_fit_average = np.average(right_fit, axis=0)

    left_line = make_cordinates(image, left_fit_average)
    right_line = make_cordinates(image, right_fit_average)

    return np.array( [ [left_line, right_line] ] )


# 함수로 처리 해보기 ( 위 순서대로 해도 됨 )
image = cv2.imread('data3/test_image.jpg')
lanelines_image = image.copy()

canny_conversion = canny_edge(lanelines_image)
cv2.imshow('canny',canny_conversion)

roi_conversion = reg_of_interest(canny_conversion)

cv2.imshow('roi', roi_conversion)   # 여기까지가 위의 함수 두개 


# 6. 선을 연결하기 위해 허프 트랜스폼 적용.  

lines = cv2.HoughLinesP( roi_conversion, 1, np.pi/180, 100, minLineLength=40, maxLineGap=50 )
# 시작선과 끝선을 리턴한다. houghlinesp

averaged_lines = average_slope_intercept(lanelines_image, lines)  # 라인 한줄로


lines_image = show_lines(lanelines_image, averaged_lines) #원래사진을 넣음 #위 함수사용

cv2.imshow('lines_image', lines_image)

# 가중치를 두어 두개 이미지 합성
combine_image = cv2.addWeighted(lanelines_image, 0.8, lines_image, 1, 1)
cv2.imshow('combined', combine_image)





## 비디오로 라인 만들기

cap = cv2.VideoCapture('data3/test2.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    #캐니 앳지에 보낸다.
    canny_image = canny_edge(frame)
    #ROI 이미지 구하기
    roi_image = reg_of_interest(canny_image)
    #허프 트랜스폼 
    lines = cv2.HoughLinesP( roi_image, 1, np.pi/180, 100, minLineLength=40, maxLineGap=5 )
    #하나의 선으로 평균선 찾기
    averaged_lines = average_slope_intercept( frame, lines )
    line_image = show_lines(frame, averaged_lines)
    combine_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow('result', combine_image)
    if cv2.waitKey(25) & 0xFF == 27 :  # 27이 esc
        break
    



cap.release()    

cv2.waitKey()
cv2.destroyAllWindows()