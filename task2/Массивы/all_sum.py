array = list(map(int, input().split()))
size = len(array)
j = 0
i = 0
while i<size:
    if i<=1000:
        j = j + 1
    i = i + 1
if j == size:
    print(sum(array))