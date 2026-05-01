n,k=map(int,input().split())
l=0
r=n
res=0
while l<=r:
    mid=l+(r-l)//2
    if (mid*(mid+3))/2>=n+k:
        res=n-mid
        r=mid-1
    else:
        l=mid+1
print(res)