def farenheit(n):
    result = int((n * (1.8))+32)
    return result

n = int(input())
C = farenheit(n)
print(C)