def solution(array, n):
    array.sort()
    res = min(array, key=lambda x: (abs(x-n), x))
    
    return res