def solution(a, d, included):
    res = 0
    
    for idx, flag in enumerate(included):
        if flag:
            res += a + idx * d
    return res