# 프로그래머스 Lv01 정수 내림차순으로 배치하기

def solution(n):
    answer = sorted(str(n), reverse=True)
    return int(''.join(answer))