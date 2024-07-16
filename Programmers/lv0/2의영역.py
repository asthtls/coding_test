def solution(arr):
    li_idx = [idx for idx,n in enumerate(arr) if n==2]
    if not li_idx:
        return [-1]
    
    start = li_idx[0]
    end = li_idx[-1]
    return arr[start:end+1]