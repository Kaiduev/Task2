n = int(input())
r = False
while n > 9:
    if n % 10 == n // 10 % 10:
        r = True
        break
    n //= 10
print('YES' if r else 'NO')