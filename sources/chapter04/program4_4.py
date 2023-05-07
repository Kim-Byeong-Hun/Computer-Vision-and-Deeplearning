# 허프변환을 이용해 공 검출하기
import cv2 as cv

img = cv.imread('soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ball = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 150, param1=150, param2=20, minRadius=50, maxRadius=120)

for i in ball[0]:
    cv.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255,0,0), 2)

cv.imshow('Ball detection', img)

cv.waitKey()
cv.destroyAllWindows()