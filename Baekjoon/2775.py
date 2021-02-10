def nfloor(b_floor, k):
    if (k > 0):
        floor = [1]
        for i in range(1, len(b_floor)):
            floor.append(floor[i - 1] + b_floor[i])
        k -= 1
        return nfloor(floor, k)
    else:
        return b_floor


for i in range(int(input())):
    k = int(input())
    n = int(input())
    floor_0 = [x for x in range(1, n + k + 1)]
    a = nfloor(floor_0, k)
    print(a[n - 1])