import cv2
import timeit

# 영상 검출기 - 사용자 정의 함수-------------------------------------------------------------------------------------
def videoDetector(cam, cascade):
    
    while True:
        
        start_t = timeit.default_timer()
         # 알고리즘 시작 시점
        """ 알고리즘 연산 """
        
        # 캡처 이미지 불러오기
        ret,img = cam.read()
        # 영상 압축
        img = cv2.resize(img,dsize=None,fx=1.0,fy=1.0)
        # 그레이 스케일 변환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        # cascade 얼굴 탐지 알고리즘 
        results = cascade.detectMultiScale(gray,            # 입력 이미지
                                           scaleFactor= 1.1,# 이미지 피라미드 스케일 factor
                                           minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                           minSize=(20,20)  # 탐지 객체 최소 크기
                                           )
                                                                           
        for box in results:
            x, y, w, h = box
            print("cx=%d, cy=%d" % ((x+w//2), (y+h//2)))
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
     
        """ 알고리즘 연산 """ 
        # 알고리즘 종료 시점
        terminate_t = timeit.default_timer()
        FPS = 'fps' + str(int(1./(terminate_t - start_t )))
        cv2.putText(img,FPS,(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
        
        
         # 영상 출력        
        cv2.imshow('facenet',img)
        
        if cv2.waitKey(1) > 0:   #1초 동안 입력된 키의 ASCII 반환값이 0보다 크면 break ('a' = 97)
            break

    cam.release()
    cv2.destroyAllWindows()

# main ------------------------------------------------------------------------------------------------------------
def main():
    # 가중치 파일 경로
    cascade_filename = 'haarcascade_frontalface_alt.xml'
    # 모델 불러오기
    cascade = cv2.CascadeClassifier(cascade_filename)

    # 영상 파일
    #cam = cv2.VideoCapture('sample.mp4')
    cam = cv2.VideoCapture(0)

    # 영상 탐지기
    videoDetector(cam, cascade)

if __name__ == '__main__':
    main()