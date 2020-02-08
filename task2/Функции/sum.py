def Sum(n):
    array = []
    size = len(n)
    i = 0
    while i < size:
        array.append(n[i])
        i = i + 1
    array = list(map(int, array))
    array.reverse()
    size2 = len(array)
    j = 0
    while j < size2:
        print(array[j],end='')
        if j==size2-1:
            print('=', end='')
        else:
            print('+', end='')
        j = j + 1
    print(sum(array))
n = input()
Sum(n)
