# 프로그래머스 입문 외계행성의 나이

def solution(age):

    answer = []
    for i in str(age):
        answer+= [chr(int(i) + 97)]
    return ''.join(answer)