def solution(n):
    res = [n]
    
    while n > 1:

        if n % 2 == 0:
            n = n/2
        elif n % 2 != 0:
            n = 3*n+1

        res.append(n)
    return res