def solution(s):
    answer = {}
    s = sorted(s[2:-2].split("},{"), key=len)
    
    for tuples in s:
        els = tuples.split(',')
        for e in els:
            number =  int(e)
            if number not in answer:
                answer[number] = 1
        
    return list(answer)