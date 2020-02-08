n = int(input())
t2 = 1
sum_ = 0
x = 0
t1 = 1
if n>0:
    while n>=t2:
        sum_ = sum_ + t2
        x = t2
        t2 = t2 + t1
        t1 = x
    print(sum_)
else:
    print('ERROR')
