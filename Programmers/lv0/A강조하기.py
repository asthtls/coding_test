def solution(myString):
    return ''.join(['A' if c.lower()=='a' else c.lower() for c in myString])