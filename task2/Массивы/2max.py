from random import randint
n = int(input())
array = [randint(-100,100) for i in range(n)]
for i in array:
    print(i, end=' ')
print()
max1 = max(array)
index1 = array.index(max1)
array.remove(max1)
max2 = max(array)
index2 = array.index(max2)
array.remove(max2)
print(max1, index1)
print(max2, index2)