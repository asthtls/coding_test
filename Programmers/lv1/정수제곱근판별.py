from math import sqrt
def solution(n):
    m = sqrt(n)
    
    if int(m) == m:
        return (m+1)**2
    else:
        return -1