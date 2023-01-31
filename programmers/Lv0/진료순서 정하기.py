# 프로그래머스 입문 진료순서 정하기

def solution(emergency):
    arr = sorted(emergency, reverse=True)
    return [arr.index(n)+1 for n in emergency]