def sumList(x, i = 0):
    if i >= len(x):
        return 0
    return int(x[i]) + sumList(x,i + 1)

n = str(input())
size = len(n)
i = 0
j = 0
array = []
while j<size:
    array.append(n[j])
    j = j + 1
array.reverse()
while i<size:
    print(array[i],end='')
    if i == size - 1:
        print('=', end='')
    else:
        print('+', end='')
    i = i + 1
print(sumList(n))