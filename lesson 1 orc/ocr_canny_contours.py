import cv2
import matplotlib.pyplot as plt

img = cv2.imread('F:\\python\\lesson 1 orc\\07.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 10, 250)
cv2.imwrite("edges.png", edges)
cv2.imshow("edges.png", edges)
cv2.waitKey(0)


#_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#plt.imshow(binary, cmap = "gray")
#plt.show()

#contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#image = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
#plt.imshow(img)
#plt.show()