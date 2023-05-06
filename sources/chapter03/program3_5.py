# 감마보정 실험
import cv2 as cv
import numpy as np

img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize=(0,0), fx=0.25, fy=0.25)

def gamma(f, gamma=1.0):
    f1 = f/255.0 # 정규화 / 결과가 62비트 실수형임
    return np.uint8(255*(f1**gamma)) # 8비트 정수형으로 변환

gc = np.hstack((gamma(img,0.5), gamma(img,0.75),gamma(img,1.0),gamma(img,2.0),gamma(img,3.0)))
cv.imshow('gamma', gc)

cv.waitKey()
cv.destroyAllWindows()