n,m,k=map(int,input().split())
if n>m:
    n,m=m,n
l=1
r=n*m
res=0
while l<=r:
    mid=l+(r-l)//2
    c=0
    for i in range(1,n+1):
        c+=min(m,mid//i)
    if c>=k:
        res=mid
        r=mid-1
    else:
        l=mid+1
print(res)