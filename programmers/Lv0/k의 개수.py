# 프로그래머스 입문 k의 개수

# count 함수 사용하는 방법론 1
def solution(i, j, k):
    answer = 0
    
    for n in range(i, j+1):
        answer += str(n).count(str(k))

    return answer


# 2중 for문 활용한 방법론 2
def solution(i, j, k):
    data = [x for x in range(i, j+1)]
    answer = 0
    
    for i in data:
        for n in str(i):
            if int(n) == k :
                answer += 1

    return answer