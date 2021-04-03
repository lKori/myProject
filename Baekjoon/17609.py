for i in range(int(input())):
    a = str(input())
    b = a[::-1]
    if (a == b):
        print(0)
    else:
        c = 0
        for j in a:
            if (a.count(j) % 2 != 0):
                c += 1
                a = a.replace("{}".format(j),"")
                if (c > 1):
                    print(2)
                    break
            b = a[::-1]
        if (a == b):
            print(1)
        else:
            print(2)