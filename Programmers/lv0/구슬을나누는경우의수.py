# def solution(balls, share):
#     n_f, m_f,test = 1,1,1
#     answer = 0 
#     for i in range(1, balls+1):
#         n_f *= i 
    
#     for j in range(1, share+1):
#         m_f *= j
    
#     for i in range(1, balls-share+1):
#         test *= i
    
    
#     answer = n_f/(test*m_f)
#     return int(answer)

def factorial(n):
    result = 1
    
    for i in range(1, n+1):
        result *= i
    return result

def solution(balls, share):
    
    return factorial(balls)//(factorial(balls-share) * factorial(share))