a,b = map(int, input().split())
for i in range(a,b+1):
    print(i,"*",i,"=",int(pow(i,2)),sep="")