def solution(picture, k):
    res = []
    
    for n in picture:
        row = ''.join(pixel * k for pixel in n)
            
        for _ in range(k):
            res.append(row)
    
    return res
            
    
    