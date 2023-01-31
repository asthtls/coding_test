# 프로그래머스 Lv01 자연수 뒤집어 배열로 만들기

def solution(n):
    return list(reversed([int(x) for x in str(n)]))