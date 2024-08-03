def solution(quiz):
    result = []
    for equation in quiz:
        left, right = equation.split('=')
        left = left.strip()
        right = right.strip()
        
        if eval(left) == int(right):
            result.append("O")
        else:
            result.append("X")
    
    return result