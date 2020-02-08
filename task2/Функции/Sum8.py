a, b = map(int, input().split())
if a >= 0 and a <= 7:
    if b >= 0 and a <= 7:
        sum_ = a + b
        sum_ = sum_ + 2
        print(sum_)