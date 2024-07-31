def solution(arr, k):
    res = []
    li = set()
    
    for n in arr:
        if n not in li:
            res.append(n)
            li.add(n)
            
            if len(res) == k:
                break
    while len(res) < k:
        res.append(-1)
    
    return res