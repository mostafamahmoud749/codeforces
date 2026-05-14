t=int(input())
for _ in range(t):
    n,l,r=map(int,input().split())
    a=sorted(map(int,input().split()))
    out=0
    for i in range(n-1):
        l1=i+1
        r1=n-1
        res=-1
        while l1<=r1:
            mid=l1+(r1-l1)//2
            if a[mid]+a[i]>=l:
                res=mid
                r1=mid-1
            else:
                l1=mid+1
        if res!=-1:
            l2=i+1
            r2=n-1
            res2=-1
            while l2<=r2:
                mid=l2+(r2-l2)//2
                if a[mid]+a[i]<=r:
                    res2=mid
                    l2=mid+1
                else:
                    r2=mid-1
            if res2!=-1 and res2>=res:
                out+=res2-res+1
    print(out)