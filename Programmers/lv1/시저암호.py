def solution(s, n):
    arr = list(s)
    
    for i in range(len(arr)):
        if arr[i].isupper():
            arr[i] = chr((ord(arr[i]) - ord('A') + n) % 26 + ord('A'))
        elif arr[i].islower():
            arr[i] = chr((ord(arr[i]) - ord('a') + n) % 26 + ord('a'))
    
    
    
    return "".join(arr)