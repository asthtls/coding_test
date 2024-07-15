def solution(arr, queries):    
    res = []
    
    for q in queries:
        s, e, k = q
        
        tmp = [arr[i] for i in range(s, e+1) if arr[i] > k]
        if tmp:
            res.append(min(tmp))
        else:
            res.append(-1)
    
    return res