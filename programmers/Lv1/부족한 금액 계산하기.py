# 프로그래머스 Lv01 부족한 금액 계산하기

def solution(price, money, count):
    result = sum([price*n for n in range(1,count+1)]) 
    money -= result 
    if money < 0:
        return abs(money)
    return 0