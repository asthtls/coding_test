
"""
프로그래머스 - 크기가 작은 부분문자열 
t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가
p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 반환하는 함수

t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가
p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 반환하는 함수


"""

def solution(t, p):
    p_len = len(p)
    cnt = 0 
    for i in range(len(t) - p_len + 1):
        temp = t[i:i+p_len]
        
        if int(temp) <= int(p):
            cnt += 1
    
    
    return cnt