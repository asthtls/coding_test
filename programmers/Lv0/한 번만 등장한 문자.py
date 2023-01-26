# 프로그래머스 입문 한 번만 등장한 문자

# 방법 1
def solution(s):
    answer = sorted(s)
    cnt_word = sorted(list(set(s)))

    return_answer = ''
    for i in range(len(cnt_word)):
        if answer.count(cnt_word[i]) == 1:
            return_answer += cnt_word[i]
            
    return return_answer
    
# 방법 2
def solution(s):
    return ''.join([n for n in sorted(s) if s.count(n) == 1])