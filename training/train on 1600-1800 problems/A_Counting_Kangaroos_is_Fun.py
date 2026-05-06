n=int(input())
a=[]
for i in range(n):
    k=int(input())
    a.append(k)
a.sort()
lb=n//2
c=n
for i in range(n//2):
    l=lb
    r=n-1
    res=-1
    while l<=r:
        mid=l+(r-l)//2
        if a[mid]>=a[i]*2:
            res=mid
            r=mid-1
        else:
            l=mid+1
    if res!=-1:
        lb=res+1
        c-=1
print(c)