# 비디오에서 수집한 영상을 이어붙이기

import cv2 as cv
import numpy as np
import sys

cap=cv.VideoCapture(0, cv.CAP_DSHOW) # 웹캠 연결시도 / 웹캠 1개일 경우 0으로 설정

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

frames = []
while True:
    ret, frame = cap.read()          # 비디오 구성 프레임 획득

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    cv.imshow('Video display', frame)

    key = cv.waitKey(1)              # 1밀리초동안 키보드 입력 기다림
    if key==ord('c'):
        frames.append(frame)
    if key==ord('q'):                # q 키가 들어오면 루프를 빠져나감
        break

cap.release()                        # 카메라 연결 종료
cv.destroyAllWindows()

if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))

    cv.imshow('collected images', imgs)

    cv.waitKey()
    cv.destroyAllWindows()

len(frames)
frames[0].shape
type(imgs)
imgs.shape