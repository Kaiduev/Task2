def reduct(M, N):
    if M>=1 and M<=pow(10,9) and N>=1 and N<=pow(10,9):
        M1 = M
        N1 = N
        while M != 0 and N != 0:
            if M > N:
                M = M % N
            else:
                N = N % M
        result = M+N
        print('GCD(',M1,',',N1,')=', result, sep='')

m,n = map(int,input().split())
reduct(m,n)
