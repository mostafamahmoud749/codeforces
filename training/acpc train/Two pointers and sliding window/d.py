t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=sorted(map(int,input().split()))
    res=0
    i=0
    j=0
    c=0
    while i<n:
        c+=a[i]
        while a[i]-a[j]>1:
            c-=a[j]
            j+=1
        while c>m:
            c-=a[j]
            j+=1
        res=max(res,c)
        i+=1
    print(res)