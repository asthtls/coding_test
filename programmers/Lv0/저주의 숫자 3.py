# 프로그래머스 입문 Lv0 저주의 숫자 3

def solution(n):
    number = 0
    for i in range(n):
        number+=1
        while number%3 == 0 or '3' in str(number):
            number += 1
            
    return number