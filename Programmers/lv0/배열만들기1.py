def solution(n, k):
    res = [i for i in range(k, n+1) if i%k == 0]
    return res