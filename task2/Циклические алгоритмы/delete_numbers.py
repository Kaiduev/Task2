n = int(input())
if n>=1 and n<=1000000000:
    n = str(n)
    array = []
    size = len(n)
    i = 0
    while i < size:
        array.append(n[i])
        i=i+1
    array = list(map(int, array))
    for i in array:
        if (i % 2) == 0:
            array.remove(i)
    for i in array:
        print(i, end="")
