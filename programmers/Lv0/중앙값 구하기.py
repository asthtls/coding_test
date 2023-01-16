# 프로그래머스 입문 중앙값 구하기

# 방법론 1
def solution(array):
    return sorted(array)[len(array)//2]

# 방법론 2
import numpy as np
def solution(array):
    return np.median(array)

# 방법론 3
import numpy as np
solution = lambda array : np.median(array)