import cv2
import imutils

cv2.namedWindow("Original")
cv2.namedWindow("Recorte 1")
cv2.namedWindow("Recorte 2")
cv2.namedWindow("Recorte 3")
cv2.namedWindow("Recorte 4")

vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()

else:
    rval = False

while rval:
  
    video_zoom = imutils.resize(frame, width=350)

    cv2.imshow('Original',video_zoom)
    Corte1 = frame[0:240, 0:320]
    cv2.imshow('Recorte 1', Corte1)
    Corte2 = frame[240:480, 0:320]
    cv2.imshow('Recorte 2', Corte2)
    Corte3 = frame[0:240, 320:640]
    cv2.imshow('Recorte 3', Corte3)
    Corte4 = frame[240:480, 320:640]
    cv2.imshow('Recorte 4', Corte4)

    rval, frame = vc.read()
   
    key = cv2.waitKey(20)
    if key == 27:
        break

