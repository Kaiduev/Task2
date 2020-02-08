A1,A2,N = map(int,input().split())
if A1>=1 and A1<=pow(10,3):
    if A2>=1 and A2<=pow(10,3):
        if N>=3 and N<=pow(10,3):
            d = A2 - A1
            An = A1 + (N-1)*d
            print(An)