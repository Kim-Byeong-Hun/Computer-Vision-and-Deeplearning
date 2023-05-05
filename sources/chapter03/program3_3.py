# 오츄 알고리즘으로 이진화하기
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

t, bin_img = cv.threshold(img[:,:,2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오추 알고리즘이 찾은 최적 임곗값=',t)

cv.imshow('R Channel', img[:,:,2])
cv.imshow('R Channel binarization', bin_img)

cv.waitKey()
cv.destroyAllWindows()