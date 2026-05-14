t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    p=list(map(int,input().split()))
    sa=a.copy()
    sa.sort()
    olda=[]
    while olda!=a:
        olda=a.copy()
        for i in range(m):
            if a[p[i]-1]>a[p[i]]:
                a[p[i]-1],a[p[i]]=a[p[i]],a[p[i]-1]
    if a==sa:
        print("YES")
    else:
        print("NO")