# 프로그래머스 입문 개미 군단

def solution(hp):
    
    general = hp // 5
    soldier = (hp - (general * 5)) // 3
    worker = (hp - (general * 5) - (soldier * 3) ) // 1
    return general + soldier + worker