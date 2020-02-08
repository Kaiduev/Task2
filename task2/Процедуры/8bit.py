def BinaryCode(n):
    if n>=0 and n<256:
        bin = ''
        while n>0:
            bin = str(n%2)+bin
            n = n//2
        print(int(bin))

n = int(input())
BinaryCode(n)