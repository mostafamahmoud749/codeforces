def can(mid):
    curt=t.copy()
    for i in range(mid+1):
        curt[a[i]-1]=0
    j=0
    for i in range(len(curt)):
        if curt[i]==p[j]:
            j+=1
        if j>=len(p):
            break
    if j>=len(p):
        return True
    return False
t=list(input().strip())
p=list(input().strip())
a=list(map(int,input().split()))
res=0
l=0
r=len(t)-1
while l<=r:
    mid=l+(r-l)//2
    if can(mid):
        res=mid+1
        l=mid+1
    else:
        r=mid-1
print(res)