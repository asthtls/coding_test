def solution(intStrs, k, s, l):
    res = []
    
    for n in intStrs:
        tmp = int(n[s:s+l])
        if tmp > k:
            res.append(tmp)
    
    return res