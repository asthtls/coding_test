# 프로그래머스 입문 각도기

def solution(angle):
    
    if angle >0 and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle >90 and angle <180:
        return 3
    else:
        return 4
