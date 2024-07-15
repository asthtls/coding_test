def solution(my_string, overwrite_string, s):
    len_str = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+len_str:]
    return answer