for x in range(100, 1000):
    a = 0
    for d in str(x):
        a+= int(d) ** 3
    if a == x:
        print(x)