def solution(s):
    res = []
    
    for w in s.split():
        if w == 'Z':
            if res:
                res.pop()
                
        else:
             res.append(int(w))   
        
    
    return sum(res)