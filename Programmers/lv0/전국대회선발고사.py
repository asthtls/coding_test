def solution(rank, attendance):
    li = [(r,i) for i, (r,a) in enumerate(zip(rank, attendance)) if a]
    li.sort()
    
    
    return 10000 * li[0][1] + 100 * li[1][1] + li[2][1]