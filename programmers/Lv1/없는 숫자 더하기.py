# 프로그래머스 Lv01 없는 숫자 더하기

def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer