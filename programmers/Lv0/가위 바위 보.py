# 프로그래머스 입문 가위 바위 보

def solution(rsp):
    dict = {'2':'0', '0':'5','5':'2'}
    return ''.join([dict.get(i) for i in rsp])