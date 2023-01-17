# 프로그래머스 입문 피자 나눠 먹기(2)

# piz가 6으로 나눠져 나머지가 0이 될때까지 while 반복문 실행

def solution(n):
    piz = 6
    
    while piz % n != 0:
        piz += 6
        
    return piz/6

