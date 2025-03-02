def solution(absolutes, signs):
    result = sum([n if sign else -n for n, sign in zip(absolutes, signs)])
    
    
    return result