import pytesseract
import cv2
import numpy as np
import urllib
import requests
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image

img = cv2.imread('04.png')
def url_to_image(url):
     resp = urllib.request.urlopen(url)
     image = np.asarray(bytearray(resp.read()), dtype="uint8")
     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
     return image

url = 'https://images.wbstatic.net/big/new/11590000/11593988-2.jpg'

img = url_to_image(url)
y=350
x=300
h=350
w=350
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)


#retval, img = cv2.threshold(img,200,255, cv2.THRESH_BINARY)
#img = cv2.resize(img,(0,0),fx=3,fy=3)
#img = cv2.GaussianBlur(img,(11,11),0)
#img = cv2.medianBlur(img,9)
#cv2.imshow('asd',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
txt = pytesseract.image_to_string(crop_img, lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
#txt = pytesseract.image_to_string(img, config='--psm 6')
print('recognition:', txt)