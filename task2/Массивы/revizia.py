n = int(input())
if n>=2 and n<=pow(10,3):
    array = list(map(int,input().split()))
    min1 = min(array)
    indexmin1 = array.index(min1)
    array.pop(indexmin1)
    min2 = min(array)
    if min1>min2:
        print(min2, min1)
    else:
        print(min1,min2)