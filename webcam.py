import cv2
from time import sleep # from 모듈 import 메서드

webcam = cv2.VideoCapture(0)       # 0: 장치 번호

if not webcam.isOpened():
    print("Could not open webcam")
    exit()                         # python 프롬프트 종료 명령

while webcam.isOpened():
    status, frame = webcam.read()

    print(status)
    sleep(0.1)     # time 모듈
    if status:
        cv2.imshow("Webcam test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()