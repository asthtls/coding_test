# 프로그래머스 입문 세균 증식

# 방법론 1
def solution(n, t):
    for i in range(t):
        n *= 2
    return n

# 방법론 2
def solution(n, t):
    return 2**t * n