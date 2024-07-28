def solution(arr):
    cnt = 0
    while True:
        res = []
        changed = False
        for n in arr:
            if n >= 50 and n % 2 == 0:
                new_n = n // 2
            elif n < 50 and n % 2 != 0:
                new_n = n * 2 + 1
            else:
                new_n = n
            res.append(new_n)
            if new_n != n:
                changed = True
        if not changed:
            return cnt
        arr = res
        cnt += 1