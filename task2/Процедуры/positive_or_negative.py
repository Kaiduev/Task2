def positive_or_negative(n):
    if n>0:
        return 1
    elif n==0:
        return 0
    elif n<0:
        return -1

n = int(input())
result = positive_or_negative(n)
print(result)