# 프로그래머스 입문 컨트롤 제트

def solution(s):
    answer = []
    
    for n in s.split(' '):
        try:
            answer.append(int(n))
        except:
            answer.pop()
    return sum(answer)