# 프로그래머스 입문 양꼬치

def solution(n, k):
    drink = n // 10
    answer = 12000 * n + 2000 * (k-drink)
    return answer