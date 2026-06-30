def can(mid):
    for i in range(n):
        ck=k
        need=mid
        s=False
        for j in range(i,n):
            if a[j]>=need:
                s=True
                break
            if j==n-1:
                break
            ck-=need-a[j]
            need-=1
        if s and ck>=0:
            return True
    return False


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=0
    r=(10**8)+1000
    res=-1
    while l<=r:
        mid=l+(r-l)//2
        if can(mid):
            l=mid+1
            res=mid
        else:
            r=mid-1
    print(res)