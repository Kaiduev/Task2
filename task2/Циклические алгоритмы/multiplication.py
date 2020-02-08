a,b = map(int,input().split())
if a>(-10000) and a<(10000):
    if b>(-10000) and a<(10000):
        p = 0
        i = 1
        z = b
        if b<0:
            z = -b
        while i<=z:
            p = p + a
            i = i + 1
        if b<0:
            p = -p
            print(p)