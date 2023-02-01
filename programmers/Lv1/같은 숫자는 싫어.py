# 프로그래머스 Lv01 같은 숫자는 싫어


def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr:
        if answer[-1:] == [i]:
            continue
        answer.append(i)
    
    return answer