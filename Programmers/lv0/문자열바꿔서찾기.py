def solution(myString, pat):
    res = ''.join(['B' if c == 'A' else 'A' for c in myString])
    return 1 if pat in res else 0