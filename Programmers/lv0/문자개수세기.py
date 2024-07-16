def solution(my_string):
    res = [0] * 52
    
    for c in my_string:
        if c.isupper():
            idx = ord(c) - ord('A')
        else:
            idx = ord(c) - ord('a') + 26
    
        res[idx] += 1
    return res