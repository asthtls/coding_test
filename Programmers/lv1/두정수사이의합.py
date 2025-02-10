def solution(a, b):
    answer = [n for n in range(min(a,b), max(a,b)+1)]
    return sum(answer)