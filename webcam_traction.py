from getchar import Getchar
import cv2
import serial
import numpy as np

sp = serial.Serial('com3', 9600, timeout=1)

webcam = cv2.VideoCapture(0)

pan = _pan = tilt = _tilt = 90

margin = 20

def send_pan(pan):
    tx_data = "pan" + str(pan) + "\n"
    sp.write(tx_data)
    print(tx_data)

def send_tilt(tilt):
    tx_data = "tilt" + str(tilt) + "\n"
    sp.write(tx_data)
    print(tx_data)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

def main(args == None):
    global pan
    global _pan
    global tilt
    global _tilt

    send_pan(90)
    send_tilt(90)

    kb = Getchar()
    key = ''

    while webcam.isOpened():
        status, frame = webcam.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100, 100, 100])
        upper_blue = np.array([150, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        res = cv2.bitwise_and(frame, frame, mask=mask)
        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

        _, bin = cv2.threshold(gary, 30, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = None
        largest_area = 0
        COLOR = (0, 255, 0)

        for cnt in contours
            area = cv2.contourArea(cnt)
            if area > largest_area:
                largest_area = area
                largest_contour = cnt

        if largest_contour is not None:
            if largest_area > 500:
                x, y, width, height = cv2.boundingRect(largest_contour)
                cv2.rectangle(frame, (x, y), (x+width, y+height), COLOR, 2)

                center_x = x + width//2
                center_y = y + height//2
                print("center: (%s, %s)" % (center_x, center_y))

                if center_x < 320 - margin:
                    print("pan left")
                    if pan - 1 >= 0:
                        pan = pan - 1
                        _pan = pan
                    else:
                        pan = 0
                        _pan = pan
                elif center_x > 320 + margin:
                    print("pan right")




if __name__ == '__main__':
    main()