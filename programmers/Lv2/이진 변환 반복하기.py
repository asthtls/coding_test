# 프로그래머스 Lv2 이진 변환 반복하기

def solution(s):
    zero_cnt = 0
    binary_cnt = 0
    while True:
        if s == '1':
            break
        
        binary_cnt +=1
        zero_cnt += s.count('0')
        
        s = s.replace('0','')
        
        s_len = len(s)
        
        s = bin(s_len)[2:]

        
    return [binary_cnt, zero_cnt]