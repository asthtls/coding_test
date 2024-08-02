def solution(my_string):
    li = my_string.split()
    
    res = int(li[0])
    
    for i in range(1, len(li), 2):
        opt = li[i]
        n = int(li[i+1])
    
        if opt == '+':
            res += n
        elif opt == '-':
            res -= n
    
    return res
    