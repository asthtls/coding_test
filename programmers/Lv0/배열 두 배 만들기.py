# 프로그래머스 입문 배열 두 배 만들기

# 방법론 1
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        answer.append(numbers[i] * 2)
    return answer
    
# 방법론 2
def solution(numbers):
    return [x*2 for x in numbers]