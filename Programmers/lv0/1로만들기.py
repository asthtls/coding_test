def solution(num_list):
    res = 0

    for n in num_list:
        cnt = 0 
        while n!=1:
            if n%2 == 0:
                n //= 2 
            else:
                n = (n-1)/2
            cnt += 1
        res += cnt
            
    return res