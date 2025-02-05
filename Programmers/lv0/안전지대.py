def solution(board):
    n = len(board)
    mine = set()
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        nx = i + dx
                        ny = j + dy

                        if 0 <= nx < n and 0 <= ny < n:
                            mine.add((nx, ny))
    
    
    return n*n - len(mine)