n = int(input())
if n>=1 and n<=1000000000:
    n = str(n)
    size = len(n)
    array = []
    i = 0
    even = 0
    not_even = 0
    while i<size:
        array.append(n[i])
        i = i + 1
    array = list(map(int,array))
    j = 0
    while j<size:
        if array[j]%2==0:
            even = even + 1
        if array[j]%2>0:
            not_even = not_even + 1
        j = j + 1
    print(not_even, even)