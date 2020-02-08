def expt(b, n):
    if n==0:
        return 1
    return b*expt(b, n-1)

a,b = map(int,input().split())
if a>=1 and a<=pow(10,5):
    if b>=1 and b<=63:
        i = 0
        while i<b:
            if i==b-1:
                print(str(a)+'=',end='')
            else:
                print(str(a)+'*',end='')
            i = i + 1
        print(expt(a,b))