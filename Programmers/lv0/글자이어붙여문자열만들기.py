def solution(my_string, index_list):
    res = ""
    for c in range(len(index_list)):
        res += my_string[index_list[c]]
    return res