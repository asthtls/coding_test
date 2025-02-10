def solution(n):
    ar = ''
    answer = 0
    
    while n > 0 :
        n, mod = divmod(n, 3)
        ar += str(mod)
        
    answer = int(ar, 3)
    return answer