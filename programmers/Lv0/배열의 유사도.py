# 프로그래머스 입문 배열의 유사도

# 참고
def solution(s1, s2):
    return len(set(s1)&set(s2))

# set, intersection 활용 
def solution(s1, s2):
    return len(set(s1).intersection(s2))