def solution(numLog):
    n_dict = {'1': 'w', '-1': 's', '10': 'd', '-10': 'a'}
    res = ''
    
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        res += n_dict[str(diff)]
    
    return res