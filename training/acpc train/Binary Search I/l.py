n,d=map(int,input().split())
a=list(map(int,input().split()))
res=0
for i in range(2,n):
    l=0
    r=i-1
    cres=0
    while l<=r:
        mid=(l+r)//2
        if a[i]-a[mid]<=d:
            cres=(i-mid)*(i-mid-1)//2
            r=mid-1
        else:
            l=mid+1
    res+=cres
print(res)