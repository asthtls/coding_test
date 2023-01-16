# 프로그래머스 입문 피자 나눠 먹기(1)

def solution(n):
    answer = 1
    
    while answer*7 < n:
        answer +=1 
    return answer