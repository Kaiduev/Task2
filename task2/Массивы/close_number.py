N = int(input())
lis = map(int, (input().split()))
x = int(input())
print(min(lis, key=lambda a:abs(a-x)))