def solution(myString):
    return ''.join([c if ord(c) > ord('l') else 'l' for c in myString])