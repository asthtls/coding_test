# 프로그래머스 입문 A로 B만들기

def solution(before, after):
    
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0
    