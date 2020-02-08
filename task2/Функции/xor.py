def Election(a,b):
    array = [a,b]
    count0 = array.count(0)
    count1 = array.count(1)
    if count0>count1:
        return 1
    elif count0==count1:
        return 1
    elif count1>count0:
        return 0

n = int(input())
i = 0
while i<n:
    a,b = map(int,input().split())
    result = Election(a,b)
    print(result)
    i = i + 1