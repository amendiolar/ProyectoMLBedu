
# coding: utf-8

# In[4]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[5]:


#Cargamos un video de ejemplo.
videoCaptura = cv2.VideoCapture('C:\\Users\\pc\\Dropbox\\00_Informatica\\23_Bedu\\00_Proyectos\\ETIQUETA_4X7.mp4')
#Obtenemos los Frames por segundo del video original.
fps = videoCaptura.get(cv2.CAP_PROP_FPS)
#Y leemos el primer cuadro (frame)
exito,frameAnterior = videoCaptura.read()

#Estos son los detalles del video. 
print("Tamaño de la imagen: (alto, ancho, canales)")
print(frameAnterior.shape)

#Mostramos la imagen:
plt.figure(figsize=(20,20))
plt.imshow(frameAnterior)
print("Cuadros por segundo: "+str(fps))


# In[6]:


#Hacemos una lista de Frames (Ahora vacía).
movementVideoFrames=[]

# en un ciclo (mientras haya frames...)
while exito:   
    #Leemos un frame (frame actual)
    exito,frameActual = videoCaptura.read()
    #Si pudimos leerlo
    if(exito):
        #Hacemos la resta del frame actual y el frame anterior.
        movimientoFrame = cv2.absdiff(frameActual, frameAnterior)
        #Metemos la resta en la lista de frames
        movementVideoFrames.append(movimientoFrame)
        #Y hacemos el frame actual, el anterior:
        frameAnterior = frameActual

#Terminando cerramos el video, para evitar problemas de archivos.
videoCaptura.release()


# In[7]:


#Sacamos el tamaño de la imagen.
height,width,layers=movementVideoFrames[0].shape

# Ponemos el formato como MP4 (asi lo pide la documentación...)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#Creamos un escritor de archivos de video.
videoEscritor=cv2.VideoWriter('C:\\Users\\pc\\Dropbox\\00_Informatica\\23_Bedu\\00_Proyectos\\ETQ_4x7_movement.mp4',fourcc,fps,(int(width),int(height)))

for counter in range(len(movementVideoFrames)):
    videoEscritor.write(movementVideoFrames[counter])
videoEscritor.release()

