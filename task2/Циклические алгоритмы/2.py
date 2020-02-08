n = int(input())
if n>=1 and n<=1000000000:
    n = str(n)
    array = []
    i = 0
    size = len(n)
    if (size%2)>0:
        while i<size:
            array.append(n[i])
            i = i + 1
        array = list(map(int,array))
        sum_ = sum(array)
        print(sum_)
    elif (size%2)==0:
        half = size/2
        while i<half:
            array.append(n[i])
            i = i + 1
        array = list(map(int,array))
        sum_ = sum(array)
        print(sum_)