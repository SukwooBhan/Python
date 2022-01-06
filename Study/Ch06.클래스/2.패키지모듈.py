"""
날짜 : 20222/01/06
이름 : 반석우
내용 : 파이썬 패키지와 모듈 실습하기 교재 P175

패키지 : 모듈파일이 있는 폴더
모듈  : 파이썬 파일(확장자.py)
"""

from Study.Lib.calc import *
import  Study.Lib.calc as c
r1 = plus(1, 2)
r2 = minus(1, 2)
r3 = multi(2, 3)
r4 = div(8, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)