import pytesseract
import cv2
import numpy as np


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

for i in range (1, 4):
	img = cv2.imread(f"media/{i}.png")
	y = 250
	x = 250
	h = 550
	w = 550
	crop_img = img[y:y + h, x:x + w]
	txt = pytesseract.image_to_string(crop_img, lang='eng', config='--psm 6 -c tessedit_char_whitelist=0123456789')
	print('recognition:', txt)
	cv2.imshow('Result', crop_img)
	cv2.waitKey(0)