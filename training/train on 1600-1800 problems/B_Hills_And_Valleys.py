def hillorvally(i):
    if i>=n-1 or i<=0: return 0
    if (a[i]>a[i-1] and a[i]>a[i+1]) or (a[i]<a[i-1] and a[i]<a[i+1]):
        return 1
    return 0

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    c=0
    if n<3:
        print(0)
        continue
    p=[0]*n
    for i in range(1,n-1):
        k=hillorvally(i)
        c+=k
        p[i]=k
    r=0
    for i in range(1,n-1):
        x=a[i]
        curc=p[i-1]+p[i]+p[i+1]
        m=curc
        a[i]=a[i-1]
        m=min(m,hillorvally(i-1)+hillorvally(i)+hillorvally(i+1))
        a[i]=a[i+1]
        m=min(m,hillorvally(i-1)+hillorvally(i)+hillorvally(i+1))
        r=max(r,curc-m)
        a[i]=x
    print(c-r)