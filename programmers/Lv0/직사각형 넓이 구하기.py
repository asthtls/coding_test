# 프로그래머스 입문 직사각형 넓이 구하기

def solution(dots):
    weight = max(dots)[0] - min(dots)[0]
    height = max(dots)[1] - min(dots)[1]
    
    return weight*height