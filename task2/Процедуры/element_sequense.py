def requense(n):
    if n>=1 and n<=150:
        if n == 1:
            return 1
        else:
            a = n - requense(requense(n - 1))
            return a

n = int(input())
print(requense(n))