# 프로그래머스 Lv01 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    
    for i in str(s):
        if i == 'p' or i == 'P':
            p_cnt +=1
        elif i == 'y' or i == 'Y':
            y_cnt +=1
    return p_cnt == y_cnt