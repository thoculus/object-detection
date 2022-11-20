#Kütüphaneleri import etme.
import cv2
import numpy as np
import matplotlib.pyplot as plt
#Fotoğrafı import edip ekrana gösterme.
img = cv2.imread('Glasses.jpeg')
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Fotoğrafın pixel değerlerini gösterip fotoğrafı resize etme.
print(img.shape) # Pixel değerini ekrana yazdırma.
imgResize = cv2.resize(img,(1000,1000)) # Fotoğrafı resize etme.(önce width sonra height değerleri girilir!)
cv2.imshow('ImageResized',imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Contour oluşturup pixel değerlerini ekrana bastırma
imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.resize(imGray,(12,16))
ret,tresh = cv2.threshold(imGray,127,255,0)
contours,hierarchy = cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(contours[2])
cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.imshow('ContourImage',img)
cv2.imshow('GrayImage',imGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Fotoğrafı pixel değerleri görünecek şekilde bastırma.
plt.imshow(img)