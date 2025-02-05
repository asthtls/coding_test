def solution(keyinput, board):
    
    x = board[0] // 2
    y = board[1] // 2
    result = [0,0]
    
    for k in keyinput:
        
        if k == 'left' and result[0] > -x:
            result[0] -= 1
        elif k == 'right' and result[0] < x:
            result[0] += 1
        elif k == 'up' and result[1] < y:
            result[1] += 1
        elif k == 'down' and result[1] > -y:
            result[1] -= 1
        
            
    return result