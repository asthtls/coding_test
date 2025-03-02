"""
프로그래머스 Lv1 - 최소직사각형 



"""


def solution(sizes):
    max_w = 0 
    max_h = 0 
    
    for n in sizes:
        width, height = max(n), min(n)
        
        max_w = max(max_w, width)
        max_h = max(max_h, height)
    
    
    return max_w*max_h