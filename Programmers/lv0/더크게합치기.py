def solution(a, b):
    one = str(a) + str(b)
    two = str(b) + str(a)
    
    if int(one) >= int(two):
        return int(one)
    else:
        return int(two)
