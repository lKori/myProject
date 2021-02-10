import math

m, n = map(int, input().split())
prime = [x for x in range(2, 1001)]
for i in range(2, 33):
    b += [x for x in range(i * 2, 1001, i)]
b = set(b)
for j in b:
    if (j in prime):
        prime.remove(j)

a = [x for x in range(m, n+1)]
if (1 in a):
    a.remove(1)
for i in prime:
    j = i
    while ((i * j <= n) or (i ** j <= n)):
        if (i * j in a):
            a.remove(i * j)
        elif (i ** j in a):
            a.remove(i ** j)
        else:
            j += 1

print(*a[:], sep = '\n')