###################################################
######### EJEMPLO 1 camara_simple.py  #############
### Elaboró: Osbaldo Aragón Banderas    ###########
## Fecha: 12/enero/2019, Guadalupe Victoria, Dgo ##
###################################################
#  El siguiente programa captura un frame de la   # 
#  cámara web conectada en la PC con el índice(0),#
#  en caso de tener más cámaras conectadas o que  #
#  no sea el índice correcto, se puede cambiar    #
#  el valor, espera la tecla ESC para salir   #####
###################################################

import cv2 #Importamos Librería OpenCV2

#Creamos una ventana con OpenCV llamada "Captura"
cv2.namedWindow(“Captura")
#Abrimos la cámara en el índice (0)
vc = cv2.VideoCapture(0)

# Si se logró abrir, se realiza la lectura de un frame y rval = TRUE
if vc.isOpened():
  rval, frame = vc.read()
else:
  rval = False
# Se captura cada frame y se muestra en la ventana "Captura"
while rval:
  cv2.imshow(“Captura", frame)
  rval, frame = vc.read()
  key = cv2.waitKey(20) #esperamos 20 ms por una tecla
  if key == 27: # Si la tecla es ESC, salimos del programa
    break
 # Cerramos la ventana creada
 cv2.destroyWindow(“Captura")
