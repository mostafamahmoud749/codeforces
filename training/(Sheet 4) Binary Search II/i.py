def can(mid):
    ck=k
    for i in range(n):
        if a[i]*mid>b[i]:
            ck-=(a[i]*mid)-b[i]
        if ck<0:
            break
    if ck<0:
        return False
    return True


n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

l=1
r=2*(10**18)
res=0
while l<=r:
    mid=l+(r-l)//2
    if can(mid):
        l=mid+1
        res=mid
    else:
        r=mid-1

print(res)
