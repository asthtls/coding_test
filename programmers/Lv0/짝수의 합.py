# 프로그래머스 입문 짝수의 합 

def solution(n):
    answer = sum([x for x in range(0, n+1, 2)])
    return answer