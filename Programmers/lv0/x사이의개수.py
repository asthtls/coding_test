def solution(myString):
    res = myString.split('x')
    return [len(c) for c in res]