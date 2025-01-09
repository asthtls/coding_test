def solution(n):
    fac = 1
    i = 0
    
    while fac <= n:
        i += 1
        fac *= i
    
    return i-1