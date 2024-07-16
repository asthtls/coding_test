def solution(my_string):
    res = [my_string[i:] for i in range(len(my_string))]
    res = sorted(res)
    
    return res