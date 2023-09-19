import cv2
import numpy as np

webcam = cv2.VideoCapture(0)       # 0: 장치 번호

if not webcam.isOpened():
    print("Could not open webcam")
    exit()                         # python 프롬프트 종료 명령

while webcam.isOpened():           # isOpened() => true, false 반환
    # 웹캠 읽어들임
    status, frame = webcam.read()

    # BGR -> HSV 로 컨버팅
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # blue 색 영역 정의
    lower_blue = np.array([100,100,120])          # range of blue 100
    upper_blue = np.array([150,255,255])          # range of blue 150

    # blue 색 영역으로 마스크 생성
    mask_b = cv2.inRange(hsv, lower_blue, upper_blue)  # color range of blue

    # 웹캠 영상과 blue 마스크를 AND 연산
    res_b = cv2.bitwise_and(frame, frame, mask=mask_b)  # apply blue mask

    # bounding box 생성을 위한 그레이 스케일로 변환
    gray = cv2.cvtColor(res_b, cv2.COLOR_BGR2GRAY)

    # 그레이 스케일로 변환된 영상을 이진화
    _, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    # 흑백 영상의 등고선
    contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 사용할 변수값 초기화
    largest_contour = None
    largest_area = 0
    COLOR = (0, 255, 0) # green color

    # contours에 저장된 1byte정보들을 순차적으로 읽어들여 가장 큰 값을 swap
    for cnt in contours:                # find largest blue object
        #print("cnt", cnt)
        area = cv2.contourArea(cnt)
        if area > largest_area:
            largest_area = area         #큰 값을 swap
            largest_contour = cnt       #큰 값을 swap

    # largest_contour가 None이 아니고 면적이 500이상 일 때
    if largest_contour is not None:
        if largest_area > 500:  # draw only larger than 500
            x, y, width, height = cv2.boundingRect(largest_contour) # 사각박스 영역 정보 반환
            cv2.rectangle(frame, (x, y), (x + width, y + height), COLOR, 2) # 원본 영상에 박스 그리기
            center_x = x + width//2      # //: 몫만 구하기
            center_y = y + height//2
            print("center: ( %s, %s )" % (center_x, center_y))

    # 웹캠 영상 출력
    cv2.imshow("VideoFrame", frame)
    #cv2.imshow('blue', res_b)

    # 'q'키 값이 입력되면 break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()             # 웹캠 닫기
cv2.destroyAllWindows()      # 모든 cv window 닫기