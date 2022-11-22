#Kütüphaneleri import etme.
import cv2
import numpy as np

shapeX = 0
shapeY = 0
num = 0

# import matplotlib.pyplot as plt
#Fotoğrafı import edip ekrana gösterme.
font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.imread('ball2.jpeg', cv2.IMREAD_COLOR)
img = cv2.imread('ball2.jpeg', cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Fotoğrafın pixel değerlerini gösterip fotoğrafı resize etme.
print(img.shape) # Pixel değerini ekrana yazdırma.
contours, _= cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(contours[2])

for cnt in contours :
  
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
  
    # draws boundary of contours.
    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5) 
  
    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    n = approx.ravel() 
    i = 0
  
    for j in n :
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]
            shapeX += x
            shapeY += y
            num += 1
        i = i + 1

#coordinates of the center of the object with respect to our image
coorX = shapeX/num
coorY = shapeY/num

print(shapeX, shapeY)
print(num)
print(coorX,coorY)

# String containing the co-ordinates.
string = str(coorX) + " " + str(coorY) 
  
# text on remaining co-ordinates.
cv2.putText(img2, string, (int(coorX), int(coorY)), font, 0.5, (0, 255, 0))
cv2.circle(img2, (int(coorX), int(coorY)), 7, (255, 255, 255), -1) 

cv2.imshow('image2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()