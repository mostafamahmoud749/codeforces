t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=p[i-1]+a[i-1]
    out=0
    for i in range(1,n+1):
        v=p[i]-k
        res=-1
        l=0
        r=i
        while l<=r:
            mid=l+(r-l)//2
            if p[mid]>=v:
                res=mid
                r=mid-1
            else:
                l=mid+1
        if res!=-1:
            out+=i-res
    print(out)