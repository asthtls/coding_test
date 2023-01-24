# 프로그래머스 입문 n의 배수 고르기

def solution(n, numlist):
    answer = [x for x in numlist if x%n == 0]
    return answer