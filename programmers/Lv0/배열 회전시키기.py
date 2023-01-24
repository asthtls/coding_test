# 프로그래머스 입문 배열 회전시키기

def solution(numbers, direction):
    answer = 0
    if direction == 'right':
        answer = [numbers[-1]] + numbers[:len(numbers)-1]
    else:
        answer = numbers[1:] + [numbers[0]]
    return answer