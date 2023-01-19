# 프로그래머스 입문 최댓값 만들기

def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]