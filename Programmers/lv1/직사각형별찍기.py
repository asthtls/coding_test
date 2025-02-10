a, b = map(int, input().strip().split(' '))

print("",end='')

star = '*' * a

for i in range(b):
    print(star, end='')
    print()