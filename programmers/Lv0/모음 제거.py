# 프로그래머스 입문 모음 제거

def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    for i in vowel:
        if i in my_string:
            my_string = my_string.replace(i, '')
    
    return my_string