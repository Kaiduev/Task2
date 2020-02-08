def revers(*args):
    list_ = sorted(args)
    for i in list_:
        print(i,end=' ')

A,B,C = map(int,input().split())
if A>=1 and A<=pow(10,4):
    if B>=1 and B<=pow(10,4):
        if C>=1 and C<=pow(10,4):
            revers(A,B,C)

