import cv2
import numpy as np
import serial
import time


img = cv2.imread("origin.png", cv2.IMREAD_COLOR)  # read image

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    # Convert from BGR to HSV

# define range of blue color in HSV
lower_blue = np.array([100,100,120])          # range of blue
upper_blue = np.array([150,255,255])

lower_green = np.array([50, 150, 50])         # range of green
upper_green = np.array([80, 255, 255])

lower_red = np.array([0, 50, 50])             # range of red
upper_red = np.array([30, 255, 255])

# Threshold the HSV image to get only blue colors
mask_b = cv2.inRange(hsv, lower_blue, upper_blue)     # color range of blue
mask_g = cv2.inRange(hsv, lower_green, upper_green)  # color range of green
mask_r = cv2.inRange(hsv, lower_red, upper_red)      # color range of red

# Bitwise-AND mask and original image
res_b = cv2.bitwise_and(img, img, mask=mask_b)      # apply blue mask
res_g = cv2.bitwise_and(img, img, mask=mask_g)    # apply green mask
res_r = cv2.bitwise_and(img, img, mask=mask_r)    # apply red mask

cv2.imshow('blue', res_b)           # show applied blue mask
cv2.imwrite("blue.png", res_b)
cv2.imshow('Green', res_g)          # show applied green mask
cv2.imwrite("green.png", res_g)
cv2.imshow('red', res_r)            # show applied red mask
cv2.imwrite("red.png", res_r)

cv2.waitKey(3000)                            # 3초 후 자동 종료
cv2.destroyAllWindows()

#    k = cv2.waitKey(5) & 0xFF
#    if k == 27:
#        break


