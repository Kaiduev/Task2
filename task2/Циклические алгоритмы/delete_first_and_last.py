n = int(input())
if n >= 1 and n <= 1000000000:
    n = str(n)
    size = len(n)
    i = 0
    array = []
    while i < size:
        array.append(n[i])
        i = i + 1
    array.remove(array[0])
    array.remove(array[len(array)-1])
    for i in array:
        print(i, end="")