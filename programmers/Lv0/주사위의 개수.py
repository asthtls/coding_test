# 프로그래머스 입문 주사위의 개수

def solution(box, n):
    return ((box[0]//n) * (box[1]//n) * (box[2]//n))