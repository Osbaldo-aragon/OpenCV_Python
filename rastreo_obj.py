import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture(0)
while(1):
  _, frame = cap.read()
  frame = imutils.resize(frame, width=800)
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
  lower = np.array([137,153,149])
  upper = np.array([174,246,227])
  
  mask = cv2.inRange(hsv, lower, upper)
  mask = cv2.erode(mask, None, iterations=2)
  mask = cv2.dilate(mask, None, iterations=2)
  
  contours= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
  res = cv2.bitwise_and(frame,frame, mask= mask)
  if len(contours) > 0:
    c = max(contours, key=cv2.contourArea)
    
    rect = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(frame,[box],0,(0,255,0),2)
    
    ((x1, y1), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    cv2.circle(frame, center, 5, (0, 255, 0), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,str(center),(center[0]-30,center[1]-50), font, 1,(0,255,0),2)
    cv2.imshow('frame',frame)
    mask = imutils.resize(mask, width=300)
    res = imutils.resize(res, width=300)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
      break
      
cv2.destroyAllWindows()
cap.release()
