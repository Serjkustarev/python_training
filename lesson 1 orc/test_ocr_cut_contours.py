import cv2
import numpy as np

img = cv2.imread("F:\\python\\lesson 1 orc\\media\\1.png")

height, width, channels = img.shape     #shape of original image

height_2 = height * 7/100
width_2 = width * 15/100

#img[0:height_2, 0:width_2] = [0, 0, 0]    #get rid of the watermark on the top left

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,15,255,cv2.THRESH_BINARY)

_, contours, _= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key=cv2.contourArea)

x,y,w,h = cv2.boundingRect(cnt)

crop = img[y:y+h,x:x+w]
#cnt = max(contours, key=cv2.contourArea)
height_2, width_2, channels_2 = crop.shape
print("height: " + repr(height_2))
print("width: " + repr(width_2))


cv2.waitKey(0)
cv2.destroyAllWindows()