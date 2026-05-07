t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(map(int,input().split()))
    mex=0
    newa=[a.pop()]
    n -= 1
    for i in range(n):
        if a[i]==mex:
            mex+=1
            newa.append(a[i])
            a[i]=-1
        elif a[i]==mex-1:
            continue
        else:
            break
    for i in range(n-1,-1,-1):
        if a[i]!=-1:
            newa.append(a[i])
    res=0
    maxel=0
    mex=0
    s=set()
    for i in range(len(newa)):
        s.add(newa[i])
        while mex in s:
            mex+=1
        maxel=max(maxel,newa[i])
        res+=mex+maxel
    print(res)