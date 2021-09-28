import cv2
import matplotlib.pyplot as plt

img = cv2.imread('F:\\python\\lesson 1 orc\\media\\2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#plt.imshow(binary, cmap = "gray")
#plt.show()

#contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#image = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)


def segment(image, threshold=25):
    global bg
    # find the absolute difference between background and current frame
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # threshold the diff image so that we get the foreground
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

    # get the contours in the thresholded image
    (_, cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # return None, if no contours detected
    if len(cnts) == 0:
        return
    else:
        # based on contour area, get the maximum contour which is the hand
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)

    x, y, w, h = cv2.boundingRect(segmented)
    crop = gray[y:y + h, x:x + w]
    cv2.imshow('crop', crop)
    cv2.waitKey(0)


segment(img)
 #_, contours = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 #cnt = max(gray, key=cv2.contourArea)

#x,y,w,h = cv2.boundingRect(segmented)

#crop = gray[y:y+h,x:x+w]
#cv2.imshow('crop', crop)

#cv2.waitKey(0)



#plt.imshow(img)
#plt.show()