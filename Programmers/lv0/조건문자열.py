def solution(ineq, eq, n, m):
    op = ineq + ('=' if eq == '=' else '')
    
    return int(eval(f'{n}{op}{m}'))
