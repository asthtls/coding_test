"""
프로그래머스 Lv1 - 삼총사

배열이 주어졌을 때  배열 안의 정수 3개를 더하여 0 이 나오면 삼총사

"""


from itertools import combinations

def solution(number):
    answer = list(combinations(number, 3))
    
    result = sum(1 for i in range(len(answer)) if sum(answer[i]) == 0)
    
    
    return result