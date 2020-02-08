def BinaryCode(n):
    if n>=0 and n<256:
        bin = ''
        while n>0:
            bin = str(n%2)+bin
            n = n//2
        return int(bin)

a,b = map(int,input().split())
a = BinaryCode(a)
b = BinaryCode(b)
sum_ = a*b
print(BinaryCode(sum_))
