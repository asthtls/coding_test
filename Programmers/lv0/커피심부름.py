def solution(order):
    res = 0
    
    for n in order:
        if 'americano' in n or n == 'anything':
            res += 4500
        elif 'latte' in n:
            res += 5000
    return res
    