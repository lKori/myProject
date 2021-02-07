from math import ceil
a, b, v = map(int, input().split())

print(int(ceil((v - b) / (a - b))))