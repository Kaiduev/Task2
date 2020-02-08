n = int(input())
if n>=1 and n<=10**9:
    n = str(n)
    array = []
    size = len(n)
    i = 0
    while i < size:
        array.append(n[i])
        i=i+1
    array = list(map(int,array))
    delete = int(input())
    try:
        while True:
            array.remove(delete)
    except:
        for i in array:
            print(i, end="")
