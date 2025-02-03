def solution(n):
    answer = []
    tmp = n
    
    for i in range(2, n+1):
        while tmp % i == 0:
            tmp //= i 
            answer.append(i)
        if tmp == 1:
            break
            
    return sorted(list(set(answer)))