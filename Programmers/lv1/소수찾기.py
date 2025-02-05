def solution(n):
    answer = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in answer: # 배수 제거하기
            answer -= set(range(i*2, n+1, i))
    
    return len(answer)