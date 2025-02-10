def gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    while y!= 0:
        (x, y) = (y, x%y)
    return x

def solution(n, m):
    return [gcd(n,m), n*m/(gcd(n,m))]