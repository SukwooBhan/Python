"""
날짜 : 2022/01/03
이름 : 반석우
내용 : 파이썬 3장 연습문제 교재 p77
"""

import random

print('>>숫자 맞추기 게임<< ')
com = random.randint(1, 10)  # 1~10 사이 난수 정수 발생

while True:
    my = int(input('예상 숫자를 입력하시오 : '))  # 숫자 입력

    if my == com:
        print('~~성공~~')
        break

    if my > com:
        print('더 작은수 입력')
        continue

    if my < com:
        print('더 큰수 입력')
        continue