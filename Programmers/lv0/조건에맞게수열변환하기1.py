def solution(arr):
    res = []
    
    for n in arr:
        if n >=50 and n%2 == 0:
            res.append(n/2)
        elif n < 50 and n%2 != 0:
            res.append(n*2)
        else:
            res.append(n)
    
    return res