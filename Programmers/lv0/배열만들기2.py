def solution(l, r):
    res = []
    
    for n in range(l, r+1):
        if set(str(n)) <= {'0', '5'}:
            res.append(n)
        
    return res if res else [-1]