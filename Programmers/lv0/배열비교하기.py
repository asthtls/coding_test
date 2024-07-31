def solution(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    
    if sum1 > sum2:
        return 1
    elif sum1 < sum2:
        return -1
    else:
        return 0
    