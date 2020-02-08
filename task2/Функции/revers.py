def revers(n):
    n = str(n)
    array = []
    i = 0
    size = len(n)
    while i<size:
        array.append(n[i])
        i = i + 1
    array.reverse()
    array = map(int,array)
    for i in array:
        print(i,end='')

a = int(input())
revers(a)




