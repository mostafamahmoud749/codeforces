def can(mid):
    r=mid//3
    cres=a*r+b*r+c*r
    if mid%3==1:
        cres+=a
    elif mid%3==2:
        cres+=a+b
    if cres>=n:
        return True
    return False

t=int(input())
for _ in range(t):
    n,a,b,c=map(int,input().split())
    l=1
    r=2*10**9
    res=0

    while l<=r:
        mid=l+(r-l)//2
        if can(mid):
            res=mid
            r=mid-1
        else:
            l=mid+1
    print(res)