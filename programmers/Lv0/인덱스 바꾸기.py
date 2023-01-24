# 프로그래머스 입문 인덱스 바꾸기

def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    
    return ''.join(w for w in my_string)