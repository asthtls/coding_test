def solution(strArr):
    return [c.lower() if idx%2 == 0  else c.upper() for idx, c in enumerate(strArr)]