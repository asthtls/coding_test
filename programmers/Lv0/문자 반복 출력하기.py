# 프로그래머스 입문 문자 반복 출력하기

def solution(my_string, n):
    answer = []
    for i in my_string:
        answer.append(i * n)
    
    answer = ''.join(answer)
    return answer