def reduct(M, N):
    M1 = M
    N1 = N
    while M != 0 and N != 0:
        if M > N:
            M = M % N
        else:
            N = N % M
    nod = M+N
    print(int(M1/nod),end='')
    print('/',end='')
    print(int(N1/nod))
M,N = map(int,input().split())
reduct(M, N)
