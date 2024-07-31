def solution(my_str, n):
    res = []
    
    for i in range(0, len(my_str), n):
        res.append(my_str[i:i+n])
    
    return res