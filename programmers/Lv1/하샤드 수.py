# 프로그래머스 Lv01 하샤드 수

def solution(x):
    num = 0
    
    for n in str(x):
        num += int(n)
    
    return x%num == 0
    
