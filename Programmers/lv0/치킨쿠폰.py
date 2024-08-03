def solution(chicken):
    service = 0
    cpn = chicken
    
    while cpn >= 10:
        new = cpn // 10
        service += new
        cpn = (cpn%10) + new
    
    return service