# 프로그래머스 Lv01 3진법 뒤집기

def solution(n):
    answer = ''
    while n > 0:
        n, m = divmod(n, 3)
        answer += str(m)
    answer = int(answer,3)
    
    return answer