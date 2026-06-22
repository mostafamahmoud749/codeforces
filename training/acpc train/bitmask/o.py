def can(mid):
    res=0
    for i in range(30):
        if p[mid][i]-p[l-1][i]==mid-l+1:
            res |=(1<<i)
    return True if res>=k else False

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    p=[[0]*30 for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(30):
            p[i][j]=p[i-1][j]+((a[i-1]>>j)&1)
    out=[]
    for i in range(q):
        l,k=map(int,input().split())
        res=-1
        cl=l
        r=n
        while cl<=r:
            mid=cl+(r-cl)//2
            if can(mid):
                res=mid
                cl=mid+1
            else:
                r=mid-1
        out.append(res)
    print(*out)