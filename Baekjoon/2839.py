n = int(input())

if ((n == 4) or (n == 7)):
    print(-1)
elif (n % 5 == 1):
    print((n // 5) - 1 + 2)
elif (n % 5 == 2):
    print((n // 5) - 2 + 4)
elif (n % 5 == 3):
    print((n // 5) + 1)
elif (n % 5 == 4):
    print((n // 5) - 1 + 3)
else:
    print(n // 5)