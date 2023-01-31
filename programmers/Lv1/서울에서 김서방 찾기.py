# 프로그래머스 Lv01 서울에서 김서방 찾기


def solution(seoul):
    number = [n for n in range(len(seoul)) if seoul[n] == 'Kim']
    return "김서방은 " +str(number[0])+"에 있다"