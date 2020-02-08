def Election(x,y,z):
    array = [x,y,z]
    count0 = array.count(0)
    count1 = array.count(1)
    if count0>count1:
        return 0
    else:
        return 1

n = int(input())
i = 0
while i<n:
    x,y,z = map(int,input().split())
    result = Election(x,y,z)
    print(result)
    i = i + 1
