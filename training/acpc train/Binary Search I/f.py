t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=sorted(map(int,input().split()))
    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=p[i-1]+a[i-1]
    for i in range(q):
        x=int(input())
        l=0
        r=n
        res=-1
        while l<=r:
            mid=(l+r)//2
            if p[mid]<=p[-1]-x:
                res=mid+1
                l=mid+1
            else:
                r=mid-1
        print((n+1)-res) if res!=-1 else print(-1)