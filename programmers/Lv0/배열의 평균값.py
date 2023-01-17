# 프로그래머스 입문 배열의 평균값

# numpy 사용 
import numpy as np

def solution(numbers):
    return np.mean(numbers)

# 파이썬 내장 함수 사용
def solution(numbers):
    return sum(numbers) / len(numbers)