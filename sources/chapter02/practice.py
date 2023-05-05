import numpy as np
import cv2 as cv
import sys
import os
os.chdir('C:/Users/qudgn/Computer-Vision-and-Deeplearning/sources/chapter02')

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

# 문제 6
img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img, (250,120), (380,250), (0,0,255), 2)
cv.putText(img, 'Soccer Ball', (270,100), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
cv.arrowedLine(img, (315,120), (315,110), (255,255,255), 2, -1)

cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()

# 문제 7
img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+100, y+100), (0,0,255), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 50, (255,0,0), 2)
    
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# 문제 8
img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy = x,y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix,iy), (x, y), (255,0,0), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        ix,iy = x,y
    elif event == cv.EVENT_RBUTTONUP:
        cv.circle(img, (ix,iy), abs(x-ix), (255,0,0), 2)
    
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# 문제 9
img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

BrushSiz = 5
LColor, RColor = (255,0,0), (0,0,255)

def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), BrushSiz, LColor, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), BrushSiz, RColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), BrushSiz, LColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSiz, RColor, -1)

    cv.imshow('Painting', img)

cv.namedWindow('Painting')
cv.imshow('Painting', img)

cv.setMouseCallback('Painting', painting)

while(True):
    key = cv.waitKey(1)
    if key == ord('+'):
        BrushSiz += 1
    elif key == ord('-'):
        if BrushSiz <= 1:
            print('더 이상 붓 크기를 줄이지 못합니다.')
        else: BrushSiz -= 1
    elif key == ord('q'):
        cv.destroyAllWindows()
        break