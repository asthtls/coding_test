def solution(polynomial):
    const = 0 
    x_all = 0
    
    for n in polynomial.split(' + '):
        if 'x' in n:
            tmp = n[:-1]
            x_all += 1 if tmp == '' else int(tmp)
        else:
            const += int(n)
    
    answer = []
    
    if x_all > 0:
        answer.append('x' if x_all == 1 else f'{x_all}x')
    if const > 0:
        answer.append(str(const))
    
    return ' + '.join(answer) if answer else '0'