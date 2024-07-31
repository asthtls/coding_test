def solution(num, total):
    start = (total - sum(range(num)))//num
    
    return [start+i for i in range(num)]