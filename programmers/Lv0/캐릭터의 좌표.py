# 프로그래머스 입문 캐릭터의 좌표

def solution(keyinput, board):
    one_board, two_board = board[0]//2, board[1]//2
    answer = [0,0]
    
    for i in keyinput:
        if i == "left" and answer[0]-1 >= -one_board:
            answer[0] -= 1
        elif i == 'right' and answer[0]+1 <= one_board:
            answer[0] += 1
        elif i == 'up' and answer[1]+1 <= two_board:
            answer[1] += 1
        elif i == 'down' and answer[1]-1 >= -two_board:
            answer[1] -= 1
    return answer