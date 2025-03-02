def solution(a, b):

    
    result = [i*j for i,j in zip(a,b)]
    
    return sum(result)