# 프로그래머스 입문 숫자 찾기

def solution(num, k):

    for idx, data in enumerate(str(num)):
        if int(data) == k:
            return idx+1
    return -1