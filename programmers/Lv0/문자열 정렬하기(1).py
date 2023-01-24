# 프로그래머스 입문 문자열 정렬하기(1)

def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) > 47 and ord(i) < 58:
            answer.append(int(i))
    answer.sort()
    return answer