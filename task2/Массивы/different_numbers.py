N = int(input())
if N>=1 and N<=pow(10,5):
    array = list(map(int,input().split()))
    print(len(set(array)))