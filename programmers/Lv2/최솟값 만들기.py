# 프로그래머스 Lv2 최솟값 만들기


def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    answer = 0
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer