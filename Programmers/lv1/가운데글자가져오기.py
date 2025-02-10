def solution(s):
    nu = int(len(s)/2)
    if len(s) % 2 == 0:
        return s[nu-1:nu+1]
    else:
        return s[nu]