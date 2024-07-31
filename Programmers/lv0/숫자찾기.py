def solution(num, k):
    li = list(str(num))
    
    if str(k) in li:
        return li.index(str(k)) + 1
    else:
        return -1
    