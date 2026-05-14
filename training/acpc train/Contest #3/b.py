import math
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=sum(a[:k])
res=c
for i in range(k,n):
    c+=a[i]-a[i-k]
    res+=c
print(f"{res/(n-k+1):.6f}")