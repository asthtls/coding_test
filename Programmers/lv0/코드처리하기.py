def solution(code):
    mode = 0 
    res = ""
    
    for idx, c in enumerate(code):
        if c == '1':
            mode = 1 - mode
        elif (mode == 0 and idx%2 ==0) or (mode == 1 and idx%2 == 1):
            res += c

    return res if res else "EMPTY"