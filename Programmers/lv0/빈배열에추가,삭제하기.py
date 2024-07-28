def solution(arr, flag):
    res = []
    
    for i in range(len(flag)):
        if flag[i] == True:
            res.extend([arr[i]] * (arr[i] * 2))
        else:
            for _ in range(arr[i]):
                res.pop()
    return res