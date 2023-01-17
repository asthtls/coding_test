
# math ceil 함수 사용
import math

def solution(slice, n):
    return math.ceil(n/slice)


# 다른 방법론
def solution(slice, n):
    return ((n-1)// slice) +1