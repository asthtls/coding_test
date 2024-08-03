def solution(num_list):
    res = [0,0]
    
    for i in num_list:
        if i%2:
            res[1] += 1
        else:
            res[0] += 1
    
    return res