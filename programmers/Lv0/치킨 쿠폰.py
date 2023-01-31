# 프로그래머스 입문 치킨 쿠폰

def solution(chicken):
    answer = 0

    while chicken > 9:
        n, m = divmod(chicken, 10)
        answer += n
        chicken = n+m
    return answer