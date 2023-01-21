# 프로그래머스 입문 제곱수 판별하기

def solution(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    else:
        return 2
