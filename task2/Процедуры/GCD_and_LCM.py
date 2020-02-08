def reduct(M, N):
    if M>=1 and M<=10000 and N>=1 and N<=10000:
        M1 = M
        N1 = N
        while M != 0 and N != 0:
            if M > N:
                M = M % N
            else:
                N = N % M
        print('GCD', M+N)
        m = M1 * N1
        while M1 != 0 and N1 != 0:
            if M1 > N1:
                M1 %= N1
            else:
                N1 %= M1
        print('LCM',m // (M1 + N1))

m,n = map(int,input().split())
reduct(m,n)