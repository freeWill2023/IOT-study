import cv2
import numpy as np
import serial
import time
def main(args=None):
    global pan; global _pan; global tilt; global _tilt;
    send_pan(75)
    send_tilt(75)


while(1):
    frame = cv2.imread("origin.png", cv2.IMREAD_COLOR)
    
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # Convert from BGR to HSV

    # define range of blue color in HSV
    lower_blue = np.array([100,100,120])          # range of blue
    upper_blue = np.array([150,255,255])

    lower_green = np.array([50, 150, 50])        # range of green
    upper_green = np.array([80, 255, 255])

    lower_red = np.array([0, 50, 50])        # range of red
    upper_red = np.array([30, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask_b = cv2.inRange(hsv, lower_blue, upper_blue)     # color range of blue
    mask_g = cv2.inRange(hsv, lower_green, upper_green)  # color range of green
    mask_r = cv2.inRange(hsv, lower_red, upper_red)      # color range of red

    # Bitwise-AND mask and original image
    res_b = cv2.bitwise_and(frame, frame, mask=mask_b)      # apply blue mask
    res_g = cv2.bitwise_and(frame, frame, mask=mask_g)    # apply green mask
    res_r = cv2.bitwise_and(frame, frame, mask=mask_r)    # apply red mask
    
    gray = cv2.cvtColor(res_b, cv2.COLOR_BGR2GRAY)
    _, bin = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        
    contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    largest_contour = None
    largest_area = 0    
    
    COLOR = (0, 255, 0)
    for cnt in contours:                # find largest blue object
        area = cv2.contourArea(cnt)
        if area > largest_area:
            largest_area = area
            largest_contour = cnt
            
     # draw bounding box with green line
    if largest_contour is not None:
        #area = cv2.contourArea(cnt)
        if largest_area > 500:  # draw only larger than 500
            x, y, width, height = cv2.boundingRect(largest_contour)       
            cv2.rectangle(frame, (x, y), (x + width, y + height), COLOR, 2)
            center_x = x + width//2
            center_y = y + height//2
            #print("center: ( %s, %s )"%(center_x, center_y)) 
    #cv2.imshow("VideoFrame",frame)       # show original frame
    cv2.imshow('blue', res_b)           # show applied blue mask
    cv2.imwrite("blue.png", res_b)
    cv2.imshow('Green', res_g)          # show appliedgreen mask
    cv2.imwrite("green.png", res_g)
    cv2.imshow('red', res_r)          # show applied red mask
    cv2.imwrite("red.png", res_r)

    k = cv2.waitKey(5) & 0xFF
        
    if k == 27:
        break
   
        
capture.release()
cv2.destroyAllWindows()
