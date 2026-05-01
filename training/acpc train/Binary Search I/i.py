t=int(input())
def lsum(i,k):
    return i*k+i*(i-1)//2
for _ in range(t):
    n,k=map(int,input().split())
    l=0
    r=n
    asum=lsum(n,k)
    res=0
    while l<=r:
        mid=(r+l)//2
        ls=lsum(mid,k)
        if ls*2>=asum:
            res=mid
            r=mid-1
        else:
            l=mid+1
    if res>1:
        ans=min(abs(lsum(res,k)*2-asum),abs(lsum(res-1,k)*2-asum))
    print(ans)
