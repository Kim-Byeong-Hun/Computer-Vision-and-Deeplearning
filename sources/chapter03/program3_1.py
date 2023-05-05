# RGB 컬러 영상을 채널별로 구분해 디스플레이 하기
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('original_RGB',img)
cv.imshow('Upper left half', img[0:img.shape[0]//2, 0:img.shape[1]//2,:])
cv.imshow('Center half', img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4,:])

cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()

# 검은색 : 모든채널 어두움 / 흰색 : 모든채널 밝음
# R 채널 : 빨간색이 밝음 --- G 채널 : ---