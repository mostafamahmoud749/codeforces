n=int(input())
a=sorted(map(int,input().split()))
q=int(input())
for i in range(q):
    x=int(input())
    l=0
    r=n-1
    res=0
    while l<=r:
        mid=(l+r)//2
        if a[mid]<=x:
            res=mid+1
            l=mid+1
        else:
            r=mid-1
    print(res)