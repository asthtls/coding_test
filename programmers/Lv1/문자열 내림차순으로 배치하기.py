# 프로그래머스 Lv01 문자열 내림차순으로 배치하기

def solution(s):
    answer = sorted(s, reverse=True)
    return ''.join(answer)