n = int(input())
if n>=2 and n<=1000:
    i = 0
    array = list(map(int, input().split()))
    max_ = max(array)
    index = array.index(max_)
    array.pop(index)
    while i<len(array):
        if array[i]==max_:
            index2 = array.index(max_)
            array.pop(index2)
        i = i + 1
    print(max(array))