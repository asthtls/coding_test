def solution(n):
    res = 1
    while (res * 6) % n != 0:
        res += 1
    return res