def solution(n):
    arr = str(n)
    li = []
    for i in arr:
        li.append(i)
    li.sort(reverse=True)
    print(li)
    return int("".join(li))