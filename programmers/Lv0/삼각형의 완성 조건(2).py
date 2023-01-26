# 프로그래머스 입문 삼각형의 완성 조건

def solution(spell, dic):
    for word in dic:
        if set(spell).issubset(set(word)):
            return 1
    return 2