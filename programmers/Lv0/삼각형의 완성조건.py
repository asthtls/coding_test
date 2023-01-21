# 프로그래머스 입문 삼각형의 완성조건

def solution(sides):
    sides.sort()
    if sides[2] >= sides[0] + sides[1]:
        return 2
    
    return 1