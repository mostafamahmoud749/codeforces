def can(mid):
    global remK
    curk=k
    for i in range(n):
        if a[i]<mid:
            curk-=mid-a[i]
    if curk>=0:
        remK=curk
        return True
    return False

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=0
    r=2*(10**12)
    res=0
    remK=0
    while l<=r:
        mid=l+(r-l)//2
        if can(mid):
            res=mid
            l=mid+1
        else:
            r=mid-1
    if res==0:
        print(0)
    else:
        c=sum(1 for i in a if i>res)
        print(res*n-(n-1)+c+remK)
