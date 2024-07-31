def solution(arr):
    answer = []
    n = 0
    
    while True:

        two = 2 ** n
        if len(arr) < two:
            for i in range(two-len(arr)):
                arr.append(0)
        n+=1
        
        if two == len(arr):
            return arr
    