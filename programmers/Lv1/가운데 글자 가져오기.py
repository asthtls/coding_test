# 프로그래머스 Lv01 가운데 글자 가져오기

def solution(s):
    if len(s)%2 == 0:
        return s[int(len(s)/2)-1 : int(len(s)/2)+1]
    else:
        return s[int(len(s)/2)]