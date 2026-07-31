t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    allx=set()

    for i in range(1,n):
        allx.add(a[i]^a[i-1])

    res=float("inf")

    for x in allx:
        cres=0
        for i in range(1,n):
            v=a[i]^a[i-1]
            r=max(v,x)
            for j in range(r.bit_length()):
                if ((x>>j)&1)!=((v>>j)&1):
                    cres+=1
                
        res=min(res,cres)

    print(res)