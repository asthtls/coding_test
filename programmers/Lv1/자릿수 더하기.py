# 프로그래머스 Lv01  자릿수 더하기

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
        
    return answer