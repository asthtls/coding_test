def solution(s):
    stack = []
    
    for n in s:
        if stack and stack[-1] == n: 
            stack.pop()
        else:
            stack.append(n)
    
    return 0 if stack else 1