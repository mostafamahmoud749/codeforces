n,m=map(int,input().split())
a=sorted(map(int,input().split()))
b=list(map(int,input().split()))
out=[]
for i in b:
    l=0
    r=n-1
    res=0
    while l<=r:
        mid=(l+r)//2
        if a[mid]<=i:
            res=mid+1
            l=mid+1
        else:
            r=mid-1
    out.append(res)
print(*out)