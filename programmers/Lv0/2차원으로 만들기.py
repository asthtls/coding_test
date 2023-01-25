# 프로그래머스 입문 2차원으로 만들기


import numpy as np
def solution(num_list, n):
    answer = np.reshape(num_list, (len(num_list)//n, n)).tolist()
    return answer


# 참고할만한 코드
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer