def solution(my_string, is_prefix):
    res = [my_string[:i+1] for i in range(len(my_string))]
    return 1 if is_prefix in res else 0