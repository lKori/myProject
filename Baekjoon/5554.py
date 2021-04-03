x = 0
y = 0
for i in range(4):
    y += int(input())
x = y // 60
y = y % 60
print("{}\n{}".format(x, y))