def double_fact(n):
    res = 1
    if(n % 2 == 0):
        i = 2
        while i <= n:
            res = res * i
            i = i + 2
        print(res)
    else:
        j = 1
        while j <= n:
            res = res * j
            j = j + 2
        print(res)

n = int(input())
double_fact(n)