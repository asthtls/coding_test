# 프로그래머스 Lv01 정수 제곱근 판별

import math

def solution(n):
    square = int(math.sqrt(n))
    
    if square*square  == n:
        return (square+1)*(square+1)
    return -1