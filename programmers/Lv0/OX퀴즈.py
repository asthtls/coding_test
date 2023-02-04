# 프로그래머스 입문 LV00 OX퀴즈

def solution(quiz):
    answer = []
    for i in quiz:
        answer.append("O" if eval(i.replace('=','==')) else "X" )
        
    return answer 