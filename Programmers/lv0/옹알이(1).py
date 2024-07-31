def solution(babbling):
    cnt = 0
    li = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for c in li:
            if c * 2 not in word:
                word = word.replace(c, ' ')
        if word.strip() == '':
            cnt += 1
    
    return cnt