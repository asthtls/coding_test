# 프로그래머스 입문 최빈값 구하기

def solution(array):
    arr = [0] * (max(array) +1)
    
    for i in array:
        arr[i] += 1
    
    most = -1
    max_idx = 0
    s_max_idx = 0
    for idx, n in enumerate(arr):
        if n > max_idx:
            most = idx
            max_idx = n
        elif n == max_idx:
            s_max_idx = n
    
    return most if max_idx != s_max_idx else -1
            
    

