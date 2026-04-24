import math


n=int(input())
a=list(map(int,input().split()))
q=int(input())
sa=a.copy()
sa.sort()
p=[0]*(n+1)
sp=[0]*(n+1)
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
for i in range(1,n+1):
    sp[i]=sp[i-1]+sa[i-1]
for i in range(q):
    m,l,r=map(int,input().split())
    if m==1:
        print(p[r]-p[l-1])
    else:
        print(sp[r]-sp[l-1])