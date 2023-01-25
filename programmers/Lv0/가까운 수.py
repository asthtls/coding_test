# 프로그래머스 입문 가까운 수 

def solution(array, n):
    array.sort()
    answer = 0
    near_data = 100
    for idx,data  in enumerate(array):
        if near_data > abs(n-data):
            near_data = abs(n-data)
            answer = data
        
    return answer