def solution(arr, intervals):
    res = []
    
    for a, b in intervals:
        res.extend(arr[a:b+1])
    return res