# SIFT 검출
import os
os.chdir('C:/Users/qudgn/Computer-Vision-and-Deeplearning/sources/chapter05')

import cv2 as cv

img = cv.imread('mot_color70.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create() # 인자를 nfeatures=500으로 바꾸면 신뢰도가 높은 500개 특징점을 얻음
kp, des = sift.detectAndCompute(gray, None)
# kp = sift.detect(gray, None) # 특징점 검출
# des = sift.compute(gray,kp) # 기술자 추출
# 이 두개를 하나의 함수로 해결

gray = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift', gray)

k = cv.waitKey()
cv.destroyAllWindows()