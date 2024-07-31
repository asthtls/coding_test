def solution(strArr):
    res = [0 for i in range(len(strArr))]
    
    for n in strArr:
        res[len(n)] += 1
    
    
    return max(res)