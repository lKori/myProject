x = int(input())

a = 0
for i in range(1, x + 2):
    if (a >= x):
        x -= a - (i - 1)
        a = i - 1
        break
    else:
        a += i

b = [x for x in range(1, a + 1)]
c = list(reversed(b))

if (a % 2 == 0):
    print("{}/{}".format(b[x-1], c[x-1]))
else:
    print("{}/{}".format(c[x-1], b[x-1]))