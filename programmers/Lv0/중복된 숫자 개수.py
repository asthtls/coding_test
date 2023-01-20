# 프로그래머스 입문 중복된 숫자 개수

# 방법론 1
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer +=1
    return answer

# 방법론 2 count 함수 사용
def solution(array, n):
    return array.count(n)