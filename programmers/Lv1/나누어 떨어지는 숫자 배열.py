# 프로그래머스 Lv01 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = sorted([n for n in arr if n%divisor==0])
    if len(answer) == 0:
        return [-1]
    
    return answer