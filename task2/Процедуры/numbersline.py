def line(n):
    array = []
    i = 0
    while i<len(n):
        array.append(n[i])
        i = i + 1
    for l in array:
        print(l)

n = str(input())
line(n)