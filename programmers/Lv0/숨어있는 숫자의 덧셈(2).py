# 프로그래머스 입문 숨어있는 숫자의 덧셈(2)

def solution(my_string):
    answer = 0

    word = ''
    
    for n in my_string:
        if n.isdecimal():
            word += n
        else:
            if len(word) == 0:
                continue
            answer += int(word)
            word= ''
    if len(word) != 0:
        answer += int(word)
    return answer