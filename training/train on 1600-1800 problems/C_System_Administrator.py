n,m,v=map(int,input().split())

if m>(n-1)*(n-2)/2+1 or m<n-1:
    print(-1)
    exit()

res=[]
if v==1:
    u=2
else:
    u=1

for i in range(1,n+1):
    if i!=v:
        res.append([v,i])

rem=m-(n-1)

if rem>0:
    for i in range(1,n+1):
        if i==v or i==u:
            continue
        for j in range(i+1,n+1):
            if j==v or j==u:
                continue

            res.append([i,j])
            rem-=1
            if rem==0:
                break
        if rem==0:
            break

for i in res:
    print(*i)