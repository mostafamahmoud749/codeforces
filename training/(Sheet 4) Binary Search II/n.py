t=int(input())
for _ in range(t):
    n=int(input())
    l=1
    r=2*10**9
    res=0
    while l<=r:
        mid=l+(r-l)//2
        if (mid*(mid-1))//2<=n:
            res=mid
            l=mid+1
        else:
            r=mid-1
    print(res+(n-(res*(res-1))//2))