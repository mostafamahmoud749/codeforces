t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    for i in range(n):
        a[i]=[a[i],i]
        b[i]=[b[i],i]
        c[i]=[c[i],i]
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    res=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if a[i][1]!=b[j][1] and a[i][1]!=c[k][1] and b[j][1]!=c[k][1]:
                    res=max(res,a[i][0]+b[j][0]+c[k][0])
    print(res)