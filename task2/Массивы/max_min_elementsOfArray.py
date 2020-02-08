import random
size = int(input())
array = [random.randint(-100, 100) for i in range(size)]
i = 0
while i < size:
    print(array[i], end=" ")
    i = i + 1
print(end="\n")
max_elem = max(array)
min_elem = min(array)
print(min_elem, array.index(min_elem))
print(max_elem, array.index(max_elem))
