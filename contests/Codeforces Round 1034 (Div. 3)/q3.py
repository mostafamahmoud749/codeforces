t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    smax=[0]*n
    smax[-1]=a[-1]
    for i in range(n-2,-1,-1):
        smax[i]=max(a[i],smax[i+1])
    res=["1"]
    mine=a[0]
    for i in range(1,n-1):
        if a[i]<=mine:
            res.append("1")
            mine=a[i]
        elif smax[i+1]>a[i]:
            res.append("0")
        else:
            res.append("1")
    res.append("1")
    print("".join(res))