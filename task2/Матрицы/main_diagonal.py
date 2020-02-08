size,line = map(int,input().split())
array = [input().split() for i in range(size)]
i = 0
j = 1
n = 0
while i<size:
    while j<line:
        array[i][j]=0
        j = j + 1
    i = i + 1
print(*[' '.join(map(str,e)) for e in array], sep='\n')