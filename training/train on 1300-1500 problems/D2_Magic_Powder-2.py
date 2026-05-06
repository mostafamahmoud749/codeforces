def can(mid):
    curk=k
    for i in range(n):
        amount=mid*req[i]
        if amount>ing[i]:
            curk-=amount-ing[i]
    if curk<0:
        return False
    else:
        return True
n,k=map(int,input().split())
req=list(map(int,input().split()))
ing=list(map(int,input().split()))
l=0
r=2*(10**18)
res=0
while l<=r:
    mid=l+(r-l)//2
    if can(mid):
        res=mid
        l=mid+1
    else:
        r=mid-1
print(res)