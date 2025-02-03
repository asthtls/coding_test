def solution(my_string):

    numbers = ''.join([c if c.isdigit() else ' ' for c in my_string])
    
    return sum(int(i) for i in numbers.split())