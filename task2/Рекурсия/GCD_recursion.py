def gcd(a, b):
    if (b > a):
        # print('GCD(' + str(b) + ',' + str(a) + ')')
        return gcd(b, a)
    r = a % b
    if (r == 0):
        return b
    else:
        # print('GCD(' + str(b) + ',' + str(a) + ')')
        return gcd(b, r)

a, b = map(int, input().split())
print(gcd(a,b))