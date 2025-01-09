def solution(emergency):
    li = list(range(1, len(emergency) + 1))
    
    sort = sorted(zip(emergency, li), key=lambda x: x[0], reverse=True)
    
    res = [0] * len(emergency)
    for n, (_, original) in enumerate(sort, 1):
        res[original-1] = n
    
    
    return res