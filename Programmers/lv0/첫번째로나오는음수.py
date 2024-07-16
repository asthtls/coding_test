def solution(num_list):
    res = [i for i,n in enumerate(num_list) if n < 0]
    return res[0] if len(res) > 0 else -1