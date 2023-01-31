# 프로그래머스 Lv01 두 정수 사이의 합


def solution(a, b):
    arr = sorted([a,b])
    return sum([n for n in range(arr[0], arr[1]+1)])