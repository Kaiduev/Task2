while True:
    a, b, c = map(int, input().split())
    list_ = [a, b, c, ]
    count1 = list_.count(a)
    count2 = list_.count(b)
    count3 = list_.count(c)
    print(max(count1, count2, count3))