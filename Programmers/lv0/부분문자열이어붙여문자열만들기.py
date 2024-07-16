def solution(my_strings, parts):
    res = ""
    
    for i in range(len(parts)):
        s, e = parts[i]
        res += str(my_strings[i][s:e+1])

    return ''.join(res)