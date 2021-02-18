a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d_max, d_min = max(a, b, c), min(a, b, c)
result = [d_max[0], d_min[1]]
if (result != a and result != b and result != c):
    print("{} {}".format(d_max[0], d_min[1]))
else:
    print("{} {}".format(d_min[0], d_max[1]))