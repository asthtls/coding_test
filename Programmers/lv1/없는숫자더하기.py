def solution(numbers):
    tmp = [n for n in range(10)]
    
    return sum(set(tmp) - set(numbers))