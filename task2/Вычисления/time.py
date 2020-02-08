a=int(input())
h=str(a//3600)
m=(a//60)%60
s=a%60
if m<10:
    m=str(m)
else:
    m=str(m)
if s<10:
    s=str(s)
else:
    s=str(s)
print(h+' '+m+' '+s)