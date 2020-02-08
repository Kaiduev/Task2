from random import randint
n = int(input())
if n>=1 and n<=pow(10,6):
    array = [randint(-100,100) for i in range(n)]
    max1 = max(array)
    count = array.count(max1)
    print(max1, count)