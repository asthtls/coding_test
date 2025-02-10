def solution(price, money, count):
    answer = 0
    
    for i in range(1,count+1):
        tmp = price * i   
        answer += tmp
    
    if money >= answer:
        return 0
    else:
        return answer - money