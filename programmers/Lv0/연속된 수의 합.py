# 프로그래머스 입문 Lv00 연속된 수의 합

def solution(num, total):
    average = total//num

    return [n for n in range(average - (num-1)//2, average + (num+2)//2)]