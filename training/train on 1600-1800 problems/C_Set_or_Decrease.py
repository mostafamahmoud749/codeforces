def can(mid):
    lo=0
    for i in range(min(n,mid+1)):
        x=mid-i
        if s-lo-a[0] + (a[0]-x)*(i+1) <= k:
            return True
        if i<n-1:
            lo+=a[n-1-i]
    return False
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=sorted(map(int,input().split()))
    s=sum(a)
    
    l=0
    r=10**15
    res=0
    while l<=r:
        mid=l+(r-l)//2
        if can(mid):
            res=mid
            r=mid-1
        else:
            l=mid+1
    print(res)