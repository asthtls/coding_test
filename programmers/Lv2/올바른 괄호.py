# 프로그래머스 Lv2 올바른 괄호

def solution(s):
    answer = []
    
    for word in s:
        if word == '(':
            answer.append(word)
        else:
            if not answer:
                return False
            answer.pop()
    return not answer