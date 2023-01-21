# 프로그래머스 입문 순서쌍의 개수

def solution(n):
    return len([x for x in range(1, n+1) if n%x == 0])