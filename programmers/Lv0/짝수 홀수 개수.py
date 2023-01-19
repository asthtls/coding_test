# 프로그래머스 입문 짝수 홀수 개수

def solution(num_list):
    answer = [0,0]
    
    for i in num_list:
        answer[i%2] += 1
    return answer