# 프로그래머스 입문 문자열 정렬하기(2)

def solution(my_string):
    my_string = my_string.lower()
    return ''.join(sorted(my_string))