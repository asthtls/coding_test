def solution(a, b, c, d):
    num = [a,b,c,d]
    set_num = set(num)
    
    if len(set_num) == 1:
        return 1111*a
        
    elif len(set_num) == 2:
        if num.count(a) == 2:
            p,q = set_num
            return (p+q) * abs(p-q)
        else:
            p = max(set_num, key=num.count)
            q = min(set_num, key=num.count)
            return (10*p+q) ** 2
        
    elif len(set_num) == 3:
        p = max(set(num), key=num.count)
        tmp = [n for n in num if n != p]
        return tmp[0] * tmp[1]

    return min(num)