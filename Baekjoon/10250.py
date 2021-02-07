for _ in range(int(input())):
    h, w, n = map(int, input().split())

    hotel = [[(j + 1) * 100 + (i + 1) for i in range(w)] for j in range(h)]

    count = 0
    for i in range(w):
        for j in range(h):
            count += 1
            if count == n:
                print(hotel[j][i])
                break