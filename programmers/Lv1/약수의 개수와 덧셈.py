# 프로그래머스 Lv01 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        cnt = 0
        for i in range(1, n//2+1):
            if n%i == 0:
                cnt += 1
        if cnt%2 != 0:
            answer += n
        else:
            answer -= n
    return answer