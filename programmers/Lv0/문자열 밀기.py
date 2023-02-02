# 프로그래머스 입문 Lv00 문자열 밀기

def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            return answer 
        A = A[-1] + A[:-1]
        answer += 1
    return -1