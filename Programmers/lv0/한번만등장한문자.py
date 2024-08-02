from collections import Counter

def solution(s):
    
    c_cnt = Counter(s)
    
    unique = [c for c, cnt in c_cnt.items() if cnt == 1]
    
    unique.sort()
    
    return ''.join(unique)