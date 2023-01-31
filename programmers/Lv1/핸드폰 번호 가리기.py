# 프로그래머스 Lv01 핸드폰 번호 가리기

def solution(phone_number):
    data_len = len(phone_number)
    
    return '*'*(data_len-4) + phone_number[-4:]