# 프로그래머스 입문 공 던지기

def solution(numbers, k):
    return numbers[2 * (k-1) % len(numbers)]