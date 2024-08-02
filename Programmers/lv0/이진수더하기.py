def solution(bin1, bin2):
    res = int(bin1, 2) + int(bin2, 2)
    return format(res, 'b')