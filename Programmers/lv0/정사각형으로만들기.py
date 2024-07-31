def solution(arr):
    rows = len(arr)
    cols = len(arr[0]) if arr else 0
    max_size = max(rows, cols)
    
    if rows > cols:
        for row in arr:
            row.extend([0] * (max_size - cols))
    
    elif cols > rows:
        for _ in range(max_size - rows):
            arr.append([0] * cols)
    
    return arr