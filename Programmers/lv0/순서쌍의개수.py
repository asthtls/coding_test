def solution(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                cnt += 1
            else:
                cnt += 2
    return cnt