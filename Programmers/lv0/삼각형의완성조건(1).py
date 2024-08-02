def solution(sides):
    sides.sort()
    return 1 if sides[-1] < sum(sides[:2]) else 2