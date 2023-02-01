# 프로그래머스 Lv01 이상한 문자 만들기

def solution(s):
    s = s.split(" ")
    answer = []
    for i in range(len(s)):
        for j in range(len(s[i])):        
            if j%2 == 0:
                answer.append(s[i][j].upper())
            else:
                answer.append(s[i][j].lower())
        answer.append(' ')
    return ''.join(answer[:-1])