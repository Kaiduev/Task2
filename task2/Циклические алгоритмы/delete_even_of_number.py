n = str(input())
i = 0
j = 0
array=[]
while i<len(n):
    array.append(n[i])
    i = i + 1
array = list(map(int,array))
for j in array:
    if (j%2)==0:
        array.remove(j)
print(array)
