# 프로그래머스 입문 등수 매기기

def solution(score):
    answer = []
    result = []
    for n in score:
        answer.append(sum(n)/len(n))
    
    sort_arr = sorted(answer, reverse=True)
    
    for i in answer:
        result.append(sort_arr.index(i)+1)
    
    return result