def solution(s1, s2):
    cnt = 0
    
    for c in s1:
        if c in s2:
            cnt +=1
    
    return cnt