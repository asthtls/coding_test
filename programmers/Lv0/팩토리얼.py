# 프로그래머스 입문 팩토리얼

def solution(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i

        if answer == n:
            return i
        elif answer > n:
            return i-1
    
    return 1