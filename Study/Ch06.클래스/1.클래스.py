"""
날짜 : 20222/01/06
이름 : 반석우
내용 : 파이썬 클래스 실습하기 교재 P148
"""

from Study.Lib.Account import Account

kb = Account('국민은행', '101-11-1011', '김유신', 10000)
kb.deposit(30000)
kb.withdraw(2500)
kb.show()

wr = Account('우리은행',' 101-11-2022', '김춘추', 20000)
wr.deposit(35000)
wr.withdraw(5000)
kb.show()
