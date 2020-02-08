n = int(input())
for i in range(1,n):
    for j in str(i):
        ji = int(j)
        if ji != 0 and ji != 1 and i % ji:
            break
    else:
        print(i,end=' ')