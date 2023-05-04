import numpy as np
import cv2 as cv
import sys

# 문제 1
a = np.array([400,52,'tiger','24',230])

# 문제 2-2
a = np.array([4,5,0,1,2,3,6,7,8,9,10,11])
print(a.min())
print(a.max())
print(a.argmin())
print(a.argmax())
print(a.mean())
print(a.sum())
print(a.cumsum())
print(a.prod())
print(a.cumprod())

# 문제 3
img1 = cv.imread('soccer.jpg')
img2 = cv.imread('soccer_gray.jpg')

if img1 is None:
    sys.exit('1번 파일을 찾을 수 없습니다.')
elif img2 is None:
    sys.exit('2번 파일을 찾을 수 없습니다.')

cv.imshow('Image1 Display', img1)
cv.imshow('Image2 Display', img2)

cv.waitKey()
cv.destroyAllWindows()

# 문제 4
img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)              # 컬러를 흑백으로 변경
for i in range(1,11):
    gray_small=cv.resize(gray,dsize=(0,0),fx=i*0.1,fy=i*0.1)
    cv.imshow('Gray image small{}'.format(i), gray_small)

cv.waitKey()
cv.destroyAllWindows()

# 문제 5
cap=cv.VideoCapture(0, cv.CAP_DSHOW) # 웹캠 연결시도 / 웹캠 1개일 경우 0으로 설정

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

while True:
    ret, frame = cap.read()          # 비디오 구성 프레임 획득

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    cv.imshow('Video display', frame)

    key = cv.waitKey(1)              # 1밀리초동안 키보드 입력 기다림
    if key==ord('g'):
        while True:
            ret, frame = cap.read()          # 비디오 구성 프레임 획득
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('Video display', frame_gray)
            key = cv.waitKey(1)
            if key==ord('c'):
                break
    if key==ord('q'):                # q 키가 들어오면 루프를 빠져나감
        break
    
cap.release()                        # 카메라 연결 종료
cv.destroyAllWindows()