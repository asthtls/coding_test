def solution(myString):
    res = myString.split('x')
    res.sort()
    
    return [c for c in res if c]