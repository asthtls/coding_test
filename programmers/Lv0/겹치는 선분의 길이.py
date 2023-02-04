# 프로그래머스 입문 LV00 겹치는 선분의 길이

def solution(lines):
    line_li = [set([]) for _ in range(200)]
    for idx, line in enumerate(lines):
        x,y = line
        for i in range(x,y):
            line_li[i + 100].add(idx)
    cnt = 0
    for line in line_li:
        if len(line) > 1:
            cnt +=1
    return cnt