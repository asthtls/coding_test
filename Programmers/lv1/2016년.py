def solution(a, b):
    d = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = b-1
    for i in range(a-1):
        answer += m[i]
    
    return d[answer%7]