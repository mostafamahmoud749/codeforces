import math


n,k=map(int,input().split())
a=list(map(int,input().split()))
db={0:1}
p=[0]*(n+1)
res=0
for i in range(1,n+1):
    if a[i-1]%k==0:
        p[i]=p[i-1]+1
    else:
        p[i]=p[i-1]
for i in range(1,n+1):
    rem=p[i]%k
    if rem in db:
        res+=db[rem]
    db[rem]=db.get(rem,0)+1
print(res)
