# 프로그래머스 입문 소인수분해

def solution(n):
    number = [x for x in range(2,n+1)]
    answer = []
    for i in number:
        while n%i == 0:
            n/= i
            answer.append(i)

    return sorted(list(set(answer)))