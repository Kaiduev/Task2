from random import randint
size,X = map(int,input().split())
array = [randint(0, 5) for i in range(size)]
index_array = []
i = 0
while i<size:
    if array[i] == X:
        index_array.append(i)
    i = i + 1
for j in array:
    print(j,end=' ')
print()
for i in index_array:
    print(i)
