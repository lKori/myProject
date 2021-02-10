import math

for i in range(int(input())):
    x, y = map(int, input().split())
    if (y - x == 1):
        print(1)
    else:
        print(math.ceil((y - x) / 2) + 1)