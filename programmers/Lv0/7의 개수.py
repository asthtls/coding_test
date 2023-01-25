# 프로그래머스 입문 7의 개수


# 내 풀이
def solution(array):
    answer = ""
    
    for i in array:
        answer += str(i)
    
    return answer.count('7')

# 다른 사람 풀이

def solution(array):
    return str(array).count("7")

