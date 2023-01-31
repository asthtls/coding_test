# 프로그래머스 입문 중복된 문자 제거

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))