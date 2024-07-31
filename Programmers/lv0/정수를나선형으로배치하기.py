def solution(n):
    res = [[0 for _ in range(n)] for _ in range(n)]
    
    x, y = 0, 0
    dx, dy = 0, 1
    
    for i in range(1, n*n + 1):
        res[x][y] = i
        
        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or res[nx][ny] != 0:
            dx, dy = dy, -dx
            nx, ny = x + dx, y + dy
        
        x, y = nx, ny
    
    return res