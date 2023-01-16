# 프로그래머스 입문 분수의 덧셈

#방법론 1
def gcd(x,y):
    if x%y == 0:
        return y
    return gcd(y, x%y)

def solution(numer1, denom1, numer2, denom2):
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    gcd_value = gcd(boonmo, boonja)
    
    answer = [boonja/gcd_value, boonmo/gcd_value]
    return answer


# 방법론 2
import math

def solution(numer1, denom1, numer2, denom2):
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    gcd_value = math.gcd(boonmo, boonja)
    
    answer = [boonja/gcd_value, boonmo/gcd_value]
    return answer

