"""
날짜 : 2022/01/04
이름 : 반석우
내용 : 파이썬 연습문제
"""

score = int(input('점수 입력 : '))
grade = None

print('입력한 점수는 %d점 이고, 등급은 ' % score, end = '')

if score >= 90:
   grade = 'A'
elif score < 90 and score >= 80:
    grade = 'B'
elif score < 80 and score >= 70:
    grade = 'C'
elif score < 70 and score >= 60:
    grade = 'D'
else:
    grade = 'F'

print('%s입니다.' % grade)

