n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=[0]*(n+1)
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
for i in range(m):
    l=0
    r=n
    res=0
    while l<=r:
        mid=l+(r-l)//2
        if p[mid]>=b[i]:
            res=mid
            r=mid-1
        else:
            l=mid+1
    print(res,b[i]-p[res-1])

