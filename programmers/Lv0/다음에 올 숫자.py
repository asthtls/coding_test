# 프로그래머스 입문 Lv00 다음에 올 숫자

def solution(common):
    arithmetric = common[1] - common[0]

    if common[1] + arithmetric == common[2]: # 등차수열
        return common[len(common)-1] + arithmetric
    else:
        return common[len(common)-1] * (common[1]//common[0])
