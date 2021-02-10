m, n = map(int, input().split())
a = []
for i in range(m, n + 1):
    count = 0
    for j in range(1, i + 1):
        if (i // j == i / j):
            count += 1
            if (count > 2):
                break
    if (count == 2):
        a.append(i)

print(*a[:], sep = '\n')