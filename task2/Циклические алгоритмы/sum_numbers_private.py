def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)



n = int(input())
if n>-100000 and n<100000:
    print(fibonacci(n))