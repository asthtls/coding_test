# 백준 2753번 윤년

Day = int(input())


if ((Day%4 == 0) and (Day%100 != 0)) or (Day%400 == 0):
    print("1")
else:
    print("0")
