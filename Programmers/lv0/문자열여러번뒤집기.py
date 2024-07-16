def solution(my_string, queries):
    my_str = list(my_string)

    for s,e in queries:
        my_str[s:e+1] = my_str[s:e+1][::-1]
    
    return ''.join(my_str)