def solution(myStr):
    res = []
    
    for i in ['a','b','c']:
        myStr = myStr.replace(i, ' ')
    
    res = myStr.split()
    
    return res or ['EMPTY']