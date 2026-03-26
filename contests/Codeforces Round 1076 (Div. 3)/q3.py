t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a[-1]=max(a[-1],b[-1])
    for i in range(n-2,-1,-1):
        a[i]=max(a[i],a[i+1],b[i])
    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=p[i-1]+a[i-1]
    res=[]
    for i in range(q):
        l,r=map(int,input().split())
        res.append(p[r]-p[l-1])
    print(*res)