def solution(my_string, s, e):
    li_str = list(my_string)
    li_str[s:e+1] = li_str[s:e+1][::-1]
    return ''.join(li_str)