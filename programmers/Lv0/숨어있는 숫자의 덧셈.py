# 프로그래머스 입문 숨어있는 숫자의 덧셈

def solution(my_string):
    answer = 0
    for i in my_string:
        if ord(i) > 47 and ord(i) <58:
            answer += int(i)
            
    return answer