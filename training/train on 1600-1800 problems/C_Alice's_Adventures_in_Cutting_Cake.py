t=int(input())
for _ in range(t):
    n,m,v=map(int,input().split())
    a=list(map(int,input().split()))

    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=p[i-1]+a[i-1]

    l=[-1]
    csum=0
    for i in range(n):
        csum+=a[i]
        if csum>=v:
            l.append(i)
            csum=0
    
    r=[n]
    csum=0
    for i in range(n-1,-1,-1):
        csum+=a[i]
        if csum>=v:
            r.append(i)
            csum=0
    
    if len(l)-1<m:
        print(-1)
        continue
    # print(p)
    # print(l)
    # print(r)
    res=-1
    for i in range(m+1):
        cl=l[i]
        cr=r[m-i]
        if cl<cr:
            res=max(res,p[cr]-p[cl+1])
    print(res)

