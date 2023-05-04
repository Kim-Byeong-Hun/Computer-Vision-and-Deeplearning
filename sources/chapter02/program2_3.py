# 영상을 흑백 영상으로 변환하고 반으로 축소하기

import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)              # 컬러를 흑백으로 변경
gray_small=cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5) # 반으로 축소

cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)

cv.imshow('Color image', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)

cv.waitKey()
cv.destroyAllWindows()