import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def nothing(x):
    pass
img = np.zeros((10,512,3), np.uint8)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 512, 400)
cv2.namedWindow('res',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('H_low','image',0,255,nothing)
cv2.createTrackbar('H_high','image',0,255,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('S_high','image',0,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)
cv2.createTrackbar('V_high','image',0,255,nothing)
while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    H_low = cv2.getTrackbarPos('H_low','image')
    H_high = cv2.getTrackbarPos('H_high','image')
    S_low = cv2.getTrackbarPos('S_low','image')
    S_high = cv2.getTrackbarPos('S_high','image')
    V_low = cv2.getTrackbarPos('V_low','image')
    V_high = cv2.getTrackbarPos('V_high','image')
    lower_HSV = np.array([H_low,S_low,V_low])
    upper_HSV = np.array([H_high,S_high,V_high])
    mask = cv2.inRange(hsv, lower_HSV, upper_HSV)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('image',img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
