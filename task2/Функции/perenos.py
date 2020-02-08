def perenos(a,b):
    count = 0
    while ((a % 10 == 1 or a % 10 == 0) and a):
        a = a / 10
    while (a % 10 != 0):
        a = a / 10
        count = count + 1
    if count>0:
        print(count)

a,b=map(int,input().split())
perenos(a,b)

