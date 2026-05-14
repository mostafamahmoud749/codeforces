n,k=map(int,input().split())
a=sorted(map(int,input().split()))
if k==0:
    print(1) if a[0]>1 else print(-1)
else:
    res=a[k-1]
    if k<n and a[k]==res:
        print(-1)
    else:
        print(res)