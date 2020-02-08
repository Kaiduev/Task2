from math import sqrt
X1,Y1,X2,Y2,X3,Y3 = map(float,input().split())
S = 0.5*abs((X1-X3)*(Y2-Y3)-(X2-X3)*(Y1-Y3))
a = sqrt(pow(X2-X1,2)+pow(Y2-Y1,2))
b = sqrt(pow(X3-X1,2)+pow(Y3-Y1,2))
c = sqrt(pow(X3-X2,2)+pow(Y3-Y2,2))
p = (a+b+c)
print(p,end=' ')
print(S)
