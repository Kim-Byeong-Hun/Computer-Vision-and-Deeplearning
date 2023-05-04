# 영상 파일을 읽고 윈도우에 디스플레이 하기

import os
os.chdir('C:/Users/qudgn/Computer-Vision-and-Deeplearning/sources')

import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyAllWindows()

type(img)
img.shape #BGR순

print(img[0,0,0], img[0,0,1], img[0,0,2]) # (0,0)화소
print(img[0,1,0], img[0,1,1], img[0,1,2]) # (0,1)화소