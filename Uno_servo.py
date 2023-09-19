import serial # 설치된 패키지인 경우
from getchar import Getchar # 작성된 파일인 경우
#from '파일명' import '클래스명'

sp = serial.Serial('COM3', 9600, timeout=1)

kb = Getchar()

key = ''
while key != 'Q':
    key = kb.getch()         # Getchar 클래스의 getch 메서드
    if key == '.':
        sp.write('.'.encode())
    elif key == ',':
        sp.write(','.encode())
    else:
        pass
