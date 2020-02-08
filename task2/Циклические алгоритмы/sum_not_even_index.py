n = int(input())
if n>=1 and n<=1000000000:
    n = str(n)
    i = 0
    array = []
    size = len(n)
    while i<size:
        array.append(n[i])
        i = i + 1
    array = list(map(int, array))
    sum_ = array[0]
    j = 1
    while j<size:
        if j%2==0:
            sum_ += array[j]
        j = j + 1
    print(sum_)
