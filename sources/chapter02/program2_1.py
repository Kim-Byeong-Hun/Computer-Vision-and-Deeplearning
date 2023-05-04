# numpy.ndarray 클래스 형의 객체를 만들고 멤버함수 적용하기

import numpy as np

a=np.array([4,5,0,1,2,3,6,7,8,9,10,11])
print(a)
print(type(a))
print(a.shape)
a.sort()
print(a)

b=np.array([-4.3,-2.3,12.9,8.99,10.1,-1.2])
b.sort()
print(b)

c=np.array(['one','two','three','four','five','six','seven'])
c.sort()
print(c)

# 멤버함수 목록 확인
dir(c)

# 멤버함수 사용법 확인
help(a.sort)