def solution(a, b):
    n1, n2 = str(a), str(b)
    
    answer = max(int(n1 + n2), 2*a*b)
    
    return answer