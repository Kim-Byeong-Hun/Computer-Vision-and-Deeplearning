# 영상에 도형을 그리고 글자쓰기

import os
os.chdir('C:/Users/qudgn/Computer-Vision-and-Deeplearning/sources/chapter02')
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img, (250,120), (380,250), (0,0,255), 2)
cv.putText(img, 'Soccer Ball', (270,110), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()

img.shape